"""@package python101
Documentation for this module.
More details.
"""

import random


def getCommonElements(a,b):
    """Documentation for a method. list_confusion."""
    try:
        alen = len(a)
        blen = len(b)
    except Exception as error:
        raise ValueError('Invalid entry exception')
    
    #print("First list:",a, " size: ",len(a))
    #print("Second list:",b, " size: ",len(b))
    listOfCommonItems = []
    for i in range(len(a)):
        iteration_counter = 0
        for j in range(len(b)):
            iteration_counter +=1
            if a[i] == b[j] and b[j] not in listOfCommonItems:
                listOfCommonItems.append(a[i])
        #print(i,":",a[i], " reviewed against ", iteration_counter," numbers:",b)
    return listOfCommonItems

#1. Randomly generate two lists to test this
def generateRandomLists():    
    sizeListA = random.randrange(10)
    sizeListB = random.randrange(10)
    randomListA = []
    randomListB = []
    for i in range(sizeListA):
        randomListA.append(random.randrange(100))
    for i in range(sizeListB):
        randomListB.append(random.randrange(100))
    return [randomListA,randomListB]



