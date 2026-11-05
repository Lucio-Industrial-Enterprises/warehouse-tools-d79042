import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_positive(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_whitespace_stripped(self):
        self.assertEqual(parse_quantity("  12  "), 12)

    # Regression tests per review feedback
    def test_zero_is_accepted(self):
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")
