import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """ Setting up SimpleCalculator instance """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """ Testing the addition method """
        self.assertEqual(self.calc(2, 5), 7)
        self.assertEqual(self.calc(2, -5), -3)
        self.assertEqual(self.calc(-2, 5), 3)

    def test_subtraction(self):
        """ Testing the subtraction method """
        self.assertEqual(self.calc(2, 5), -3)
        self.assertEqual(self.calc(12, 5), 7)

    def test_multiplication(self):
        """ Testing the subtraction method """
        self.assertEqual(self.calc(2, 5), 10)
        self.assertEqual(self.calc(12, -5), -60)
        self.assertEqual(self.calc(-1, -1), 1)

    def test_division(self):
        """ Testing the subtraction method """
        self.assertEqual(self.calc(10, 5), 2)
        self.assertEqual(self.calc(0, 5), "None")






