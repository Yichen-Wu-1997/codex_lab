from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from workflow_rules.playbook import review_steps


class PlaybookTests(unittest.TestCase):
    def test_bugfix_steps_are_review_oriented(self) -> None:
        steps = review_steps("bugfix")
        self.assertIn("Read the failing test first.", steps)
        self.assertIn("Rerun tests and inspect the diff.", steps)

    def test_docs_steps_focus_on_guidance_and_explanation(self) -> None:
        steps = review_steps("docs")
        self.assertIn("Read the relevant guidance before editing.", steps)
        self.assertIn("Explain what changed and what you verified.", steps)

    def test_feature_steps_include_tests_first(self) -> None:
        steps = review_steps("feature")
        self.assertIn("Add tests for the new behavior first.", steps)

    def test_unknown_task_kind_raises(self) -> None:
        with self.assertRaises(ValueError):
            review_steps("unknown")


if __name__ == "__main__":
    unittest.main()
