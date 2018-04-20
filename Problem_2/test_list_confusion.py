"""@package python101
Documentation for this module.
More details.
"""

import unittest
from list_confusion import getCommonElements
from list_confusion import generateRandomLists


class list_confusion_test(unittest.TestCase):
    #  @param self The object pointer..
    def testA_orderedLists(self):
        self.assertEqual(getCommonElements([1,2,3],[1,2,3]),[1,2,3])
        """Documentation for a method."""
        print(".+ Test test_orderedLists Passed")
    def testB_firstListLarger(self):
        self.assertEqual(getCommonElements([1,2,3,4],[1,2,3]),[1,2,3])
        print("+ Test test_firstListLarger Passed")
    def testC_secondListLarger(self):
        self.assertEqual(getCommonElements([1,2,3],[1,2,3,4]),[1,2,3])
        print("+ Test test_secondListLarger Passed")
    def testD_firstListEmtpy(self):
        self.assertEqual(getCommonElements([],[1,2,3]),[])
        print("+ Test test_firstListEmtpy Passed")
    def testE_secondListEmpty(self):
        self.assertEqual(getCommonElements([1,2,3],[]),[])
        print("+ Test testE_secondListEmpty Passed")
    def testF_bothListsEmpty(self):
        self.assertEqual(getCommonElements([],[]),[])
        print("+ Test testF_bothListsEmpty Passed")
    def testG_unOrderedLists(self):
        self.assertEqual(getCommonElements([5,3,6,1,23,2],[3,1,2]),[3,1,2])
        self.assertEqual(getCommonElements([3,1,2],[5,3,6,1,23,2]),[3,1,2])
        print("+ Test testG_unOrderedLists Passed")
    def testH_invalidEntries(self):
        with self.assertRaises(Exception) as context:
            getCommonElements(1,"s")
            getCommonElements([1,2],[1,2,3])
        self.assertTrue(context.exception)
        print("+ Test testH_invalidEntries Passed")
    def testI_listsWithRepeatedElements(self):
        self.assertEqual(getCommonElements([1,1,2,2,3,3],[1,2,2,3]),[1,2,3])
        self.assertEqual(getCommonElements([1,2,2,3],[1,1,2,2,3,3]),[1,2,3])
        print("+ Test testH_invalidEntries Passed")
    def testJ_randomListsReceived(self):
        lists = generateRandomLists()
        self.assertTrue(isinstance(getCommonElements(lists[0],lists[1]),list))
        print("+ Test testJ_randomListsReceived Passed")
    def testK_mixedTypeElements(self):
        self.assertEqual(getCommonElements(['ba','a',3,2,'k','c'],['a',2,'l','c']),['a',2,'c'])
        self.assertEqual(getCommonElements(['ba','a',[1,2,3],2,'k','c'],['a',2,[1,2,3],'l','c']),['a',[1,2,3],2,'c'])
        print("+ Test testK_mixedTypeElements Passed")
        
        
if __name__ == "__main__":
    unittest.main()
