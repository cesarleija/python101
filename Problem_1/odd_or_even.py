#Conventions
#-Variable names: [bl][Result]

import msvcrt
from math import isclose
from subprocess import call


#isModulus2Cero
def isModulus2Cero(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False
#isMultipleOfFour
def isMultipleOfFour(number):
    if int(number) % 4 == 0:
        return True
    else:
        return False
# Checks from 0 to intNumber if a number divides with no residue intNumber
# if a number is exact divisor and not 1 or intNumber function returns False
# if loop goes al the way to intNumber, function returns True
def isNumberPrime(sNumber):
    intNumber = int(sNumber)
    divisor = 1
    while divisor <= intNumber:
        if intNumber % divisor == 0:
            if divisor != intNumber and divisor != 1:
                return False
        divisor+=1
    return True

def isInputDigit(number):
    return number.isdigit()
    

def main():
    print("-"*30)
    print("Program started.")

    number = input("->Give me a number:")
    if isInputDigit(number):
        if isModulus2Cero(number):
            if isMultipleOfFour(number):
                print("--> Even multiple of four!")
            else:
                print("--> Even number")
        else:
            print("--> Odd number")
        if isNumberPrime(number):
            print("--> Number is prime")
        else:
            print("--> Number is not prime")
        print("Program ended.")
        print("-"*30)
    else:
        print("Number is not digit, restarting...")
        call(["python", "odd_or_even.py"])

