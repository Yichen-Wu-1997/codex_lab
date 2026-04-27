from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from repo_map.inventory import sample_files
from repo_map.report import build_overview, count_by_area, find_entry_points


class ReportTests(unittest.TestCase):
    def test_count_by_area(self) -> None:
        counts = count_by_area(sample_files())
        self.assertEqual({"source": 2, "tests": 1, "docs": 1}, counts)

    def test_find_entry_points(self) -> None:
        self.assertEqual(
            ["src/repo_map/report.py", "README.md"],
            find_entry_points(sample_files()),
        )

    def test_build_overview_mentions_entry_points(self) -> None:
        overview = build_overview(sample_files())
        self.assertIn("Entry points", overview)
        self.assertIn("README.md", overview)


if __name__ == "__main__":
    unittest.main()
