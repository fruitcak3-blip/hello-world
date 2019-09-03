import math

def ad():
    lst=[]
    product=0
    len=int(input("\nPlease type in how many numbers you want to add "))
    for i in range(0,len):
        ele=int(input())
        lst.append(ele)
    for i in range(0,len):
        product=product+lst[i]
    print (product)

def mult():
    lst=[]
    product=1
    len=int(input("\nPlease type in how many numbers you want to multiply "))
    for i in range(0,len):
        ele=int(input())
        lst.append(ele)
    for i in range(0,len):
        product=product*lst[i]
    print (product)


    #add input to a list, use for loop to mult










welc = input('''Select Operation
A) Add
B) Subtract
C) Multiply
D) Divide
E) Exponents
*Integrals and derivatives soon!

''')
if(welc=="A"or welc=="Add"):
    ad()
elif(welc=="C" or welc == "Multiply"):
    mult()
