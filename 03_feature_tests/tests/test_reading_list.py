from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from feature_lab.reading_list import ReadingList


class ReadingListTests(unittest.TestCase):
    def test_add_book_increases_total(self) -> None:
        reading_list = ReadingList()
        reading_list.add_book("Deep Work", "Cal Newport")
        self.assertEqual(1, reading_list.total_books())

    def test_mark_read_removes_title_from_unread_list(self) -> None:
        reading_list = ReadingList()
        reading_list.add_book("Deep Work", "Cal Newport")
        reading_list.add_book("Clean Code", "Robert C. Martin")

        reading_list.mark_read("Deep Work")

        self.assertEqual(["Clean Code"], reading_list.unread_titles())

    def test_mark_read_raises_for_unknown_title(self) -> None:
        reading_list = ReadingList()
        with self.assertRaises(ValueError):
            reading_list.mark_read("Missing Book")

    # Change: tests for the new search_titles feature.
    def test_search_titles_is_case_insensitive_and_preserves_order(self) -> None:
        reading_list = ReadingList()
        reading_list.add_book("Clean Code", "Robert C. Martin")
        reading_list.add_book("The Pragmatic Programmer", "Andrew Hunt")
        reading_list.add_book("Code Complete", "Steve McConnell")

        self.assertEqual(
            ["Clean Code", "Code Complete"],
            reading_list.search_titles("CoDe"),
        )

    def test_search_titles_returns_empty_list_when_nothing_matches(self) -> None:
        reading_list = ReadingList()
        reading_list.add_book("Deep Work", "Cal Newport")

        self.assertEqual([], reading_list.search_titles("python"))


if __name__ == "__main__":
    unittest.main()
