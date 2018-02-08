import unittest
from reverseword import reverseInput


class test_reverseword(unittest.TestCase):
    print()
    def testA_reverseWordRight(self):
        self.assertEqual(reverseInput("hi there"),"there hi")
        self.assertEqual(reverseInput("hi , there"),"there , hi")
        print(".Test testA_reverseWordRight passed")
    def testB_emptyString(self):
        self.assertEqual(reverseInput(""),"")
        print("Test testB_emptyString passed")

if __name__ == "__main__":
    unittest.main()
