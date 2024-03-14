import unittest
from index import ComplexCalculator

class TestComplexCalculator(unittest.TestCase):
    def setUp(self):
        num1 = (3, 2)
        num2 = (1, 7)
        num3 = (3, 2)
        num4 = (0, 0)
        num5 = (1.5, 2.5)
        num6 = (3.5, 4.5)
        self.calculator = ComplexCalculator(num1, num2)
        self.calculatorForbidden = ComplexCalculator(num3, num4)
        self.calculatorFloats = ComplexCalculator(num5, num6)

    def test_add(self):
        self.assertEqual(self.calculator.add(), (4, 9), "Addition result is incorrect")

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), (2, -5), "Subtraction result is incorrect")

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), (-11, 23), "Multiplication result is incorrect")
    
    def test_multiply_floats(self):
        self.assertEqual(self.calculatorFloats.multiply(), (-6, 15.5), "Multiplication result is incorrect")

    def test_divide(self):
      self.assertEqual(self.calculator.divide(), (0.34, -0.38), "Division result is incorrect")

    def test_divide_forbidden(self):
        self.assertEqual(self.calculatorForbidden.divide(), "Can't divide by 0", "Division result is incorrect")

if __name__ == '__main__':
    unittest.main()