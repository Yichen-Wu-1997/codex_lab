from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from bugfix_lab.booking import can_book_room


class BookingTests(unittest.TestCase):
    def test_booking_under_capacity_is_allowed(self) -> None:
        self.assertTrue(can_book_room(attendees=4, capacity=5))

    def test_booking_at_capacity_is_still_allowed(self) -> None:
        self.assertTrue(can_book_room(attendees=5, capacity=5))

    def test_booking_above_capacity_is_rejected(self) -> None:
        self.assertFalse(can_book_room(attendees=6, capacity=5))

    def test_standing_room_adds_two_people(self) -> None:
        self.assertTrue(can_book_room(attendees=7, capacity=5, allow_standing=True))
        self.assertFalse(can_book_room(attendees=8, capacity=5, allow_standing=True))


if __name__ == "__main__":
    unittest.main()
