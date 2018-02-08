import unittest
import shutil,tempfile
from os import path
from testfixtures import TempDirectory
from fileoverlap import getOverlappingNumbers
from fileoverlap import getListFromFile
from fileoverlap import storeOutput



class testing_fileoverlap(unittest.TestCase):    
    print()
    def setUp(self):
        self.testdir = tempfile.mkdtemp()        
        objFile1 = open(path.join(self.testdir, 'test1.txt'), 'w')
        objFile1.write('1\n2\n3\n')
        objFile2 = open(path.join(self.testdir, 'test2.txt'), 'w')
        objFile2.write('1\n2\n3\n')
        objFile3 = open(path.join(self.testdir, 'test3.txt'), 'w')
        objFile3.write('1\n\n3\n')
        objFile3.close()
        objFile1.close()
        objFile2.close()
    

    def tearDown(self):
        shutil.rmtree(self.testdir)
        
    def testA_providingPathToExistingFiles(self):
        self.assertEqual(getOverlappingNumbers(path.join(self.testdir, 'test1.txt')
                                               ,path.join(self.testdir, 'test2.txt'))
                         ,['1','2','3'])
        print(".Test testA_providingPathToExistingFiles passed")
    def testB_providingTheSameFile(self):
        self.assertRaises(Exception
                          ,getOverlappingNumbers
                          ,path.join(self.testdir, 'test1.txt')
                          ,path.join(self.testdir, 'test1.txt'))
        print("Test testB_providingTheSameFile passed")
    def testC_provindingPathToNotExistingFiles(self):
        self.assertRaises(Exception
                          ,getOverlappingNumbers
                          ,path.join(self.testdir, 'test5.txt')
                          ,path.join(self.testdir, 'test1.txt'))
        self.assertRaises(Exception
                          ,getOverlappingNumbers
                          ,path.join(self.testdir, 'test1.txt')
                          ,path.join(self.testdir, 'test5.txt'))
        self.assertRaises(Exception
                          ,getOverlappingNumbers
                          ,path.join(self.testdir, 'test6.txt')
                          ,path.join(self.testdir, 'test5.txt'))
        print("Test testC_provindingPathToNotExistingFiles passed")
    def testD_obtainingListFromValidFilePath(self):
        self.assertEqual(getListFromFile(path.join(self.testdir, 'test1.txt')),['1','2','3'])
        print("Test testD_obtainingListFromValidFilePath passed")
    def testE_obtaininListFromInvalidFilePath(self):
        self.assertRaises(Exception
                    ,getListFromFile
                    ,path.join(self.testdir,'test5.txt'))
        print("Test testE_obtaininListFromInvalidFilePath passed")
    def testF_oneFileWithAnEmptyLine(self):
        self.assertEqual(getOverlappingNumbers(path.join(self.testdir,'test1.txt')
                                              ,path.join(self.testdir,'test3.txt'))
                         ,['1','3'])
        print("Test testF_oneFileWithAnEmptyLine passed")
    def testG_testFinishWritting(self):
        self.assertTrue(storeOutput(['1','2','3'],path.join(self.testdir, 'output.txt')))
        print("Test testG_testFinishWritting passed")
    def testH_storingEmtpylist(self):
        self.assertTrue(storeOutput([],path.join(self.testdir, 'output.txt')))
        print("Test testH_storingEmtpylist passed")
    def testI_storedListIsRight(self):
        storeOutput(['1','2','3'],path.join(self.testdir, 'output1.txt'))
        storeOutput(['1','3'],path.join(self.testdir, 'output2.txt'))
        with open(path.join(self.testdir, 'output1.txt'),'r') as file:
            self.assertEqual(file.read().splitlines(),['1','2','3'])
        with open(path.join(self.testdir, 'output2.txt'),'r') as file:
            self.assertNotEqual(file.read().splitlines(),['1','2','3'])            
        print("Test testI_storedListIsRight passed")
    def testJ_correctQuantityOfOverlapingElements(self):
        storeOutput(['1','2','3','4'],path.join(self.testdir, 'output1.txt'))
        with open(path.join(self.testdir, 'output1.txt'),'r') as file:
            self.assertEqual(len(file.read().splitlines()),4)
        storeOutput(['1','2','3'],path.join(self.testdir, 'output1.txt'))
        with open(path.join(self.testdir, 'output1.txt'),'r') as file:
            self.assertEqual(len(file.read().splitlines()),3)
        print("Test testJ_correctQuantityOfOverlapingElements passed")    

if __name__ == "__main__":
    unittest.main()


