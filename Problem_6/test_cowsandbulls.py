import unittest
from cowsandbulls import generateFourDigitNumber
from cowsandbulls import getCowsAndBulls


class test_cowsAndBulls(unittest.TestCase):
    print()
    def setUp(self):
        self.random1 = generateFourDigitNumber()
        self.random2 = generateFourDigitNumber()
        self.random3 = generateFourDigitNumber()
    def tearDown(self):
        self.random1 = None
        self.random2 = None
        self.random3 = None
    def testA_isDigitNumber(self):
        self.assertTrue(generateFourDigitNumber().isnumeric())
        print(".Test testA_cowsAndBulls pass")
    def testB_isRandomDifferentEveryTime(self):
        self.assertNotEqual(self.random1,self.random2)
        self.assertNotEqual(self.random2,self.random3)
        self.assertNotEqual(self.random3,self.random1)
        print("Test testB_isRandomDifferentEveryTime pass")
    def testC_4cows0bulls(self):
        self.assertEqual(getCowsAndBulls("1234","4321"),[0,4])
        self.assertEqual(getCowsAndBulls("1111","1111"),[4,4])
        self.assertEqual(getCowsAndBulls("1101","1110"),[2,4])
        print("Test testC_4cows0bulls pass")
        

if __name__=="__main__":
    unittest.main()

