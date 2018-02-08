import os
from fileoverlap import getOverlappingNumbers
from fileoverlap import storeOutput

primeNumbersFilePath = os.path.join(os.path.dirname(__file__),'primenumbers.txt')
happyNumbersFilePath = os.path.join(os.path.dirname(__file__),'happynumbers.txt')

print()
print("This are the overlapping numbers:")
print()
output = getOverlappingNumbers(primeNumbersFilePath,happyNumbersFilePath)
print(output)
print()
print("Saving to output.txt")
storeOutput(output,'output.txt')


