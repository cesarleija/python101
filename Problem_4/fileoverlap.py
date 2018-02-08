import sys
sys.path.insert(0, "../Problem_2")
try:
    from list_confusion import *
except ImportError:
    print('No Import')

def getListFromFile(filePath):
    sList = []
    with open(filePath,'r') as obj:
        uList = obj.read().splitlines()
        for i in range(len(uList)):
            sList.append(uList[i])
    return sList

def getOverlappingNumbers(filePath1, filePath2):
    if filePath1 == filePath2:
        raise Exception('The paths are the same')
    sList1 = getListFromFile(filePath1)
    sList2 = getListFromFile(filePath2)
    return getCommonElements(sList1,sList2)

def storeOutput(overlappintNumbersList,outputFilePath):
    blFinishedWriting = False
    with open(outputFilePath, 'w') as objFile:
        for eachItem in overlappintNumbersList:
            objFile.write("%s\n" % eachItem)
        blFinishedWriting = True
    return blFinishedWriting




