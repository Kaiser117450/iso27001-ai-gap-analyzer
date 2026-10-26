import tempfile
import unittest
from pathlib import Path

import gap_analyzer as ga

HEADER = "id,status,risk,owner,evidence,justification\n"


def write_csv(body):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
    f.write(HEADER + body)
    f.close()
    return f.name


class GapAnalyzerTest(unittest.TestCase):
    controls = ga.load_controls()

    def test_annex_a_has_93_controls_in_4_themes(self):
        self.assertEqual(len(self.controls), 93)
        themes = {c["theme"] for c in self.controls.values()}
        self.assertEqual(themes, {"Organizational", "People", "Physical", "Technological"})

    def test_rejects_invalid_rows(self):
        bad = write_csv("9.9,implemented,3,,,\n5.1,done,3,,,\n5.2,not_applicable,3,,,\n5.3,missing,7,,,\n")
        with self.assertRaises(ValueError) as ctx:
            ga.load_assessment(bad, self.controls)
        msg = str(ctx.exception)
        for expected in ("unknown control id", "must be one of", "no justification", "risk must be"):
            self.assertIn(expected, msg)

    def test_scoring_and_gap_order(self):
        path = write_csv("6.1,implemented,3,,,\n6.2,partial,2,,,\n6.3,missing,5,,,\n"
                         "6.4,not_applicable,1,,,No staff\n")
        assessment = ga.load_assessment(path, self.controls)
        result = ga.analyze(self.controls, assessment)
        people = result["themes"]["People"]
        # 8 People controls, 1 excluded -> 7 applicable; score 1 + 0.5 = 1.5
        self.assertEqual((people["applicable"], people["excluded"]), (7, 1))
        self.assertEqual(people["pct"], round(100 * 1.5 / 7, 1))
        self.assertEqual(result["gaps"][0]["id"], "6.3")  # highest risk first
        self.assertNotIn("6.1", [g["id"] for g in result["gaps"]])

    def test_example_report_renders(self):
        example = Path(__file__).parent / "examples" / "assessment_fnb.csv"
        assessment = ga.load_assessment(example, self.controls)
        result = ga.analyze(self.controls, assessment)
        report = ga.render_report("Test", self.controls, assessment, result)
        soa = report.split("## Statement of Applicability")[1]
        self.assertEqual(soa.count("\n| ") - 1, 93)  # minus the header row


if __name__ == "__main__":
    unittest.main()
