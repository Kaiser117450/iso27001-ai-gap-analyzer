# ISO 27001 AI Gap Analyzer

![ci](https://github.com/Kaiser117450/iso27001-ai-gap-analyzer/actions/workflows/ci.yml/badge.svg)

A small, auditable tool that turns an ISO/IEC 27001:2022 self-assessment into:

- a **readiness score** per Annex A theme (Organizational, People, Physical, Technological),
- a **risk-ranked gap list**,
- a draft **Statement of Applicability (SoA)** covering all 93 Annex A controls,
- optionally, a **Claude-drafted 90-day remediation plan** (`--ai`).

Built by [Akmal Habib Marzuki](https://akmlab.vercel.app/) for the multi-brand F&B group where I run IT, to prepare its systems (POS, loyalty data, internal web apps) for ISO 27001 and Indonesia's Personal Data Protection Law (UU PDP 27/2022).

> This tool supports an ISMS project. It does not certify anything: ISO 27001 certification requires an audit by an accredited certification body.

## Quick start

```bash
python -m unittest -v                     # standard library only
python gap_analyzer.py examples/assessment_fnb.csv --org "Contoh Resto Nusantara" --out report.md
```

See [`examples/sample_report.md`](examples/sample_report.md) for the output.

With AI remediation (needs `pip install anthropic` and `ANTHROPIC_API_KEY`):

```bash
python gap_analyzer.py my_assessment.csv --org "My Company" --ai
```

`--ai` sends the top 10 gaps (control id, title, status, risk, notes) to the Claude API. Keep secrets, IP addresses and personal data out of the notes column.

## Assessment format

| column | values |
|---|---|
| `id` | Annex A control, e.g. `8.5` |
| `status` | `implemented`, `partial`, `missing`, `not_applicable` |
| `risk` | 1 (low) – 5 (critical), default 3 |
| `owner` | who closes the gap |
| `evidence` | what exists today |
| `justification` | **required** for `not_applicable` (ISO 27001 clause 6.1.3 d) |

Controls not in the file count as `not_assessed` gaps, because an auditor treats missing evidence as a missing control.

## Scoring

`implemented` = 1, `partial` = 0.5, `missing` / `not_assessed` = 0; `not_applicable` is excluded. Gaps are ordered by risk, then missing before partial, then Annex A order.

## Repository layout

```
gap_analyzer.py          CLI + library (load, validate, analyze, render, AI)
data/annex_a_2022.csv    93 Annex A control ids, themes and titles
examples/                fictional F&B assessment + generated report
docs/                    career roadmap and program application notes
```

Annex A control titles are listed for reference only; the normative text of ISO/IEC 27001 is copyrighted by ISO and is not included.
