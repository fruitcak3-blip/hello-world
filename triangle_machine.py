import math

#A^2 + B^2 + C^2
def pyth():

    var1 = int(input("What is the length of the first side? "))
    var2 = int(input("What is the length of the second side? "))
    var3 = math.sqrt(var1**2 + var2**2)
    list_sides=[var1,var2,var3]

    print("The third side is "+ str(var3)+ " units long")
    print("The hypotenuse is "+str(max(list_sides)))

#Finds the type of triangle
def typ():

    var1 = int(input("What is the length of the first side? "))
    var2 = int(input("What is the length of the second side? "))
    var3 = int(input("What is the length of the third side? "))
    list_sides=[var1,var2,var3]
    hypotenuse = max(list_sides)
    list_sides.remove(max(list_sides))

    if(var1==var2 and var2==var3 and var1==var3):
        print("The triangle is equilateral")

    elif((list_sides[0]**2+list_sides[1]**2)==hypotenuse**2):
        print("The triangle is right")

    elif(var1==var2 or var2==var3 or var1==var3):
        print("The triangle is isoceles")

    else:
        print("The triangle is scalene")

def area():

    var1 = int(input("What is the height of the triangle? "))
    var2 = int(input("What is the length of the base of the triangle? "))
    print("The area of the triangle is "+str((var1+var2)/2))



welc = input('''Welcome to program, what function would you like to execute?
A) Pythagorean theorem
B) Triange Types
C) Area of a triangle
''')

if(welc=="A"):
    pyth()

elif(welc=="B"):
    typ()

elif(welc=="C"):
    area()
