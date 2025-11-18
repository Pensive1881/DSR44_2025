# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()