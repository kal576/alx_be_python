import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """ Setting up SimpleCalculator instance """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """ Testing the addition method """
        self.assertEqual(self.calc.add(2, 5), 7)
        self.assertEqual(self.calc.add(2, -5), -3)
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_subtraction(self):
        """ Testing the subtraction method """
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(12, 5), 7)

    def test_multiplication(self):
        """ Testing the subtraction method """
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(12, -5), -60)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_division(self):
        """ Testing the subtraction method """
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(3, 0))

if __name__ == "__main__":
    unittest.main()






