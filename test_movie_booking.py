import unittest
from movie_booking import calculate_ticket_price


class TestBooking(unittest.TestCase):
    def test_valid_booking(self):
        self.assertEqual(calculate_ticket_price(200, 3), 600)

    def test_invalid_booking(self):
        with self.assertRaises(ValueError):
            calculate_ticket_price(200, 0)


if __name__ == "__main__":
    unittest.main()