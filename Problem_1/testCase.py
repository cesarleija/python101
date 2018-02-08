import unittest
from mul import multiply
from odd_or_even import isModulus2Cero

class MultiplyTestCase(unittest.TestCase):
    def test_multiplication_with_correct_values(self):
        self.assertEqual(multiply(5,5),25)


class OddOrEvenTestCase(unittest.TestCase):
    def test_isModulus2Cero_with_correct_values(self):
        self.assertEqual(isModulus2Cero(2),True)
    def test_isModulus2Cero_with_incorrect_values(self):
        self.assertFalse(isModulus2Cero(3),True)
    def test_isModulus2Cero_with_cero(self):
        self.assertTrue(isModulus2Cero(0))

if __name__ == "__main__":
    unittest.main()
