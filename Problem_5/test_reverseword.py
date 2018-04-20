"""@package \python101\Problem_5\
Documentation for this module.
More details.
"""

import unittest
from reverseword import reverseInput


class test_reverseword(unittest.TestCase):
    print()
    def testA_reverseWordRight(self):
        """Documentation for a method."""
        self.assertEqual(reverseInput("hi there"),"there hi")
        self.assertEqual(reverseInput("hi , there"),"there , hi")
        print(".Test testA_reverseWordRight passed")
    def testB_emptyString(self):
        self.assertEqual(reverseInput(""),"")
        print("Test testB_emptyString passed")

if __name__ == "__main__":
    unittest.main()
