import random
import os

def generateFourDigitNumber():
    print()
    print("Random 4-digit number generated.")
    return "".join(str(x) for x in random.sample(range(9),4))

def getCowsAndBulls(uGuess, number):
    guess  = ""
    if len(uGuess)!=4:
        raise ValueError('** Not a 4-digit number.')
    else:
        guess = uGuess
        listGuessCopy = list(guess)
        listNumberCopy = list(number)
        
        cows = 0
        bulls = 0
        
        for x in range(len(number)):
            if number[x] == guess[x]:
                cows += 1
            popedItemFromGuessCopy = listGuessCopy.pop(0)
            if  popedItemFromGuessCopy in listNumberCopy:
                listNumberCopy.remove(popedItemFromGuessCopy)
                bulls +=1
        return [cows,bulls]

def game():
    os.system('cls')
    print()
    print("*"*30)
    print("Game Cows and Bulls started")
    
    continueGame = True
    number = generateFourDigitNumber()
    tries = 0
    
    while(continueGame):
        try:    
            uGuess = input("+ Guess the number:")
            cowsandbulls = getCowsAndBulls(uGuess,number)
            if cowsandbulls[0] == 4:
                continueGame  = False
            else:
                print("* You have ", cowsandbulls[0], " cows and ", cowsandbulls[1], " bulls")
                print("guess: ",uGuess)
                print("number: ",number)
        except ValueError as v:
            print(str(v))
        finally:
            tries +=1
    print("Game Cows and Bulls ended. It took you ", tries, " tries.")
    print("Then random number was: ",number)
    print("*"*30)


    
