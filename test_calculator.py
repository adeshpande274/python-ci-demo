import unittest

from calculator import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_adds_tax(self):
        self.assertEqual(calculate_total(100, 18), 118.00)

    def test_rounds_to_two_decimal_places(self):
        self.assertEqual(calculate_total(12.51, 5), 13.14)

    def test_rejects_negative_amount(self):
        with self.assertRaises(ValueError):
            calculate_total(-1, 18)


if __name__ == "__main__":
    unittest.main()
