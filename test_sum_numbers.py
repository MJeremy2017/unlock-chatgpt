import unittest
from sum_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add_two_numbers(5, 7), 12)
        self.assertEqual(add_two_numbers(-2, 2), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add_two_numbers(3.5, 2.5), 6.0)
        self.assertAlmostEqual(add_two_numbers(-3.5, 3.5), 0.0)
        self.assertAlmostEqual(add_two_numbers(0.0, 0.0), 0.0)


if __name__ == "__main__":
    unittest.main()
