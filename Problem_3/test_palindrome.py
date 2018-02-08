import unittest
import os
from palindrome import isWordPalindrome

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__),'testdata.txt')

class palindrome_test(unittest.TestCase):
    print()
    def setUp(self):
        with open(TESTDATA_FILENAME) as f:
                self.testdata = []
                self.testdata = f.readlines()
    def testA_palindromeWords(self):
        for i in range(len(self.testdata)):
            self.assertTrue(isWordPalindrome(self.testdata[i][:-1]))
        print(".Test testA_palindromeWords pass on", i, "samples")    
    def testB_palindromeNumber(self):
        self.assertTrue(isWordPalindrome("12321"))
        self.assertTrue(isWordPalindrome("2345678765432"))
        print("Test testB_palindromeNumber pass")
    def testC_mixedPalindrome(self):
        self.assertTrue(isWordPalindrome("123x321"))
        print("Test testC_mixedPalindrome pass")
    def testD_emptyWordIsNotPalindrome(self):
        self.assertFalse(isWordPalindrome(""))
        print("Test testD_emptyWordIsNotPalindrome pass")

if __name__ == "__main__":
    unittest.main()
