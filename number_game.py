from random import *
var= input("Can you guess the random number between 1-10? ")
var2 =randint(1,10)
if(var==var2):
    print("Correct, the number was "+str(var2))
else:
    print("I'm sorry, the actual answer was "+str(var2))
