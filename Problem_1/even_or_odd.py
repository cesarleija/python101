''' Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message.  
Ask the user for two numbers: one number to check (call it num) 
and one number to divide by (check). If check divides evenly into num, tell that to the user. If not,
print a different appropriate message. 
Source:http://www.practicepython.org/
'''


num = int(input("Enter a number: "))
if num%2 ==0:
	print("This number is even")
	if num %4==0:
		print("It's also a multiple of 4")
else:
	print("This number is odd")


num = int(input("Enter another number: "))

check = int(input("Okay, last one. Another number please: "))
if num %check ==0:
	print("%d divides evenly into %d" % (check, num))
else:
	print("%d does not divide evenly into %d" % (check, num))
