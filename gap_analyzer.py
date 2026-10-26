"""ISO/IEC 27001:2022 Annex A gap analyzer.

Reads a self-assessment CSV, scores readiness per Annex A theme, and writes a
Markdown report with a prioritised gap list and a Statement of Applicability
(SoA) draft. With --ai, Claude drafts a remediation plan for the top gaps.
"""
import argparse
import csv
import sys
from pathlib import Path

DEFAULT_CONTROLS = Path(__file__).parent / "data" / "annex_a_2022.csv"
STATUS_SCORE = {"implemented": 1.0, "partial": 0.5, "missing": 0.0, "not_assessed": 0.0}
VALID_STATUS = {"implemented", "partial", "missing", "not_applicable"}
MODEL = "claude-opus-5-5"


def load_controls(path=DEFAULT_CONTROLS):
    with open(path, newline="", encoding="utf-8") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def load_assessment(path, controls):
    """Return {control_id: row}. Raises ValueError on any invalid row."""
    rows, errors = {}, []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for line, row in enumerate(csv.DictReader(f), start=2):
            cid = (row.get("id") or "").strip()
            status = (row.get("status") or "").strip().lower()
            if cid not in controls:
                errors.append(f"line {line}: unknown control id '{cid}'")
                continue
            if cid in rows:
                errors.append(f"line {line}: duplicate control id '{cid}'")
                continue
            if status not in VALID_STATUS:
                errors.append(f"line {line}: status '{status}' must be one of {sorted(VALID_STATUS)}")
                continue
            # ISO 27001 clause 6.1.3 d): every exclusion in the SoA needs a justification.
            if status == "not_applicable" and not (row.get("justification") or "").strip():
                errors.append(f"line {line}: control {cid} is not_applicable but has no justification")
                continue
            try:
                risk = int(row.get("risk") or 3)
            except ValueError:
                risk = 0
            if not 1 <= risk <= 5:
                errors.append(f"line {line}: risk must be an integer 1-5")
                continue
            rows[cid] = {
                "status": status,
                "risk": risk,
                "owner": (row.get("owner") or "").strip(),
                "evidence": (row.get("evidence") or "").strip(),
                "justification": (row.get("justification") or "").strip(),
            }
    if errors:
        raise ValueError("\n".join(errors))
    return rows


def analyze(controls, assessment):
    """Score each theme. Unassessed controls count as gaps: an auditor treats no evidence as no control."""
    themes, gaps = {}, []
    for order, (cid, ctrl) in enumerate(controls.items()):
        a = assessment.get(cid, {"status": "not_assessed", "risk": 3, "owner": "", "evidence": "", "justification": ""})
        t = themes.setdefault(ctrl["theme"], {"applicable": 0, "score": 0.0, "excluded": 0})
        if a["status"] == "not_applicable":
            t["excluded"] += 1
            continue
        t["applicable"] += 1
        t["score"] += STATUS_SCORE[a["status"]]
        if a["status"] != "implemented":
            gaps.append({"id": cid, "title": ctrl["title"], "order": order, **a})
    for t in themes.values():
        t["pct"] = round(100 * t["score"] / t["applicable"], 1) if t["applicable"] else 100.0
    applicable = sum(t["applicable"] for t in themes.values())
    overall = round(100 * sum(t["score"] for t in themes.values()) / applicable, 1) if applicable else 100.0
    # Highest risk first, then missing before partial, then Annex A order.
    gaps.sort(key=lambda g: (-g["risk"], STATUS_SCORE[g["status"]], g["order"]))
    return {"themes": themes, "overall": overall, "gaps": gaps}


def _cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def render_report(org, controls, assessment, result, top=15, ai_text=None):
    out = [f"# ISO/IEC 27001:2022 Gap Analysis: {org}", "",
           f"**Overall readiness: {result['overall']}%** "
           f"({len(result['gaps'])} open gaps across {len(controls)} Annex A controls)", "",
           "> Self-assessment only. This is not a certification; certification requires an audit "
           "by an accredited certification body.", "",
           "## Readiness by theme", "", "| Theme | Applicable | Excluded | Readiness |", "|---|---|---|---|"]
    for name, t in result["themes"].items():
        out.append(f"| {name} | {t['applicable']} | {t['excluded']} | {t['pct']}% |")

    out += ["", f"## Top {min(top, len(result['gaps']))} gaps (by risk)", "",
            "| Control | Title | Status | Risk | Owner | Notes |", "|---|---|---|---|---|---|"]
    for g in result["gaps"][:top]:
        out.append(f"| {g['id']} | {_cell(g['title'])} | {g['status']} | {g['risk']} | "
                   f"{_cell(g['owner']) or '-'} | {_cell(g['evidence']) or '-'} |")

    if ai_text:
        out += ["", "## AI-drafted remediation plan", "",
                "_Drafted by Claude. Review before use: it is a starting point, not audit evidence._", "", ai_text]

    out += ["", "## Statement of Applicability (draft)", "",
            "| Control | Title | Applicable | Status | Justification / evidence |", "|---|---|---|---|---|"]
    for cid, ctrl in controls.items():
        a = assessment.get(cid)
        status = a["status"] if a else "not_assessed"
        applicable = "No" if status == "not_applicable" else "Yes"
        note = (a["justification"] or a["evidence"]) if a else ""
        out.append(f"| {cid} | {_cell(ctrl['title'])} | {applicable} | {status} | {_cell(note) or '-'} |")
    return "\n".join(out) + "\n"


def ai_remediation(org, gaps, top=10):
    """Ask Claude for a remediation plan. Returns text, or None if unavailable."""
    try:
        import anthropic
    except ImportError:
        print("warning: 'anthropic' not installed; skipping AI section (pip install anthropic)", file=sys.stderr)
        return None
    lines = "\n".join(f"- {g['id']} {g['title']} | status={g['status']} | risk={g['risk']} | notes={g['evidence'] or '-'}"
                      for g in gaps[:top])
    prompt = (f"Organisation: {org}\n\nOpen ISO/IEC 27001:2022 Annex A gaps from a self-assessment, highest risk first:\n"
              f"{lines}\n\nWrite a practical remediation plan in Markdown. For each gap give: the concrete action, "
              "the evidence an auditor will ask for, a rough effort (S/M/L), and a suggested order across a 90-day plan. "
              "Prefer low-cost controls suitable for a small company. Do not invent facts about the organisation.")
    try:
        client = anthropic.Anthropic()
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            output_config={"effort": "medium"},
            system="You are an ISO/IEC 27001 Lead Implementer helping a small organisation close audit gaps.",
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.APIError as e:
        print(f"warning: Claude API call failed, report written without AI section: {e}", file=sys.stderr)
        return None
    if response.stop_reason == "refusal":
        print("warning: Claude declined the request; report written without AI section", file=sys.stderr)
        return None
    return "\n".join(b.text for b in response.content if b.type == "text").strip() or None


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("assessment", help="self-assessment CSV (id,status,risk,owner,evidence,justification)")
    p.add_argument("--org", default="Organisation", help="organisation name for the report")
    p.add_argument("--out", default="gap_report.md", help="output Markdown file")
    p.add_argument("--controls", default=DEFAULT_CONTROLS, help="Annex A controls CSV")
    p.add_argument("--top", type=int, default=15, help="number of gaps to list")
    p.add_argument("--ai", action="store_true", help="add a Claude-drafted remediation plan (needs ANTHROPIC_API_KEY)")
    args = p.parse_args(argv)

    controls = load_controls(args.controls)
    try:
        assessment = load_assessment(args.assessment, controls)
    except ValueError as e:
        print(f"invalid assessment:\n{e}", file=sys.stderr)
        return 2
    result = analyze(controls, assessment)
    ai_text = ai_remediation(args.org, result["gaps"]) if args.ai else None
    Path(args.out).write_text(render_report(args.org, controls, assessment, result, args.top, ai_text), encoding="utf-8")
    print(f"Overall readiness {result['overall']}% | {len(result['gaps'])} gaps | report: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
