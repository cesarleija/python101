

from list_confusion import getCommonElements
from list_confusion import generateRandomLists
import random

#Lists
#a = [1,1,2,3,4,8,13,21,34,55,89]
#b = [1,2,3,4,5,6,7,8,9,10,11,12,13]


print("-"*30)
print("List of common items:")

print(getCommonElements(random.sample(range(random.randrange(30,35)),random.randrange(10)),random.sample(range(random.randrange(30,35)),random.randrange(10))))


