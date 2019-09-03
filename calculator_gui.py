from tkinter import *
from math import *

currentvar = ""
list_num=[]
product = 0
add1=False
sub1=False
mult1=False
div1=False
tracer=False

def define1():
    global currentvar
    global label1
    currentvar=currentvar+"1"
    label1.configure(text=str(currentvar))

def define2():
    global currentvar
    global label1
    currentvar=currentvar+"2"
    label1.configure(text=str(currentvar))

def define3():
    global currentvar
    global label1
    currentvar=currentvar+"3"
    label1.configure(text=str(currentvar))

def define4():
    global currentvar
    global label1
    currentvar=currentvar+"4"
    label1.configure(text=str(currentvar))

def define5():
    global currentvar
    global label1
    currentvar=currentvar+"5"
    label1.configure(text=str(currentvar))

def define6():
    global currentvar
    global label1
    currentvar=currentvar+"6"
    label1.configure(text=str(currentvar))

def define7():
    global currentvar
    global label1
    currentvar=currentvar+"7"
    label1.configure(text=str(currentvar))

def define8():
    global currentvar
    global label1
    currentvar=currentvar+"8"
    label1.configure(text=str(currentvar))

def define9():
    global currentvar
    global label1
    currentvar=currentvar+"9"
    label1.configure(text=str(currentvar))

def define0():
    global currentvar
    global label1
    currentvar=currentvar+"0"
    label1.configure(text=str(currentvar))

def per():
    global currentvar
    global label1
    currentvar=currentvar+"."
    label1.configure(text=str(currentvar))

def add():
    global list_num
    global currentvar
    global add1
    global sub1
    global mult1
    global div1
    list_num.append(float(currentvar))
    label1.configure(text="")
    currentvar = ""
    add1=True
    sub1=False
    mult1=False
    div1=False

def sub():
    global list_num
    global currentvar
    global add1
    global sub1
    global mult1
    global div1

    list_num.append(float(currentvar))
    label1.configure(text="")
    currentvar = ""
    add1=False
    sub1=True
    mult1=False
    div1=False

def mult():
    global list_num
    global currentvar
    global add1
    global sub1
    global mult1
    global div1

    list_num.append(float(currentvar))
    label1.configure(text="")
    currentvar = ""
    add1=False
    sub1=False
    mult1=True
    div1=False

def div():
    global list_num
    global currentvar
    global add1
    global sub1
    global mult1
    global div1

    list_num.append(float(currentvar))
    label1.configure(text="")
    currentvar = ""
    add1=False
    sub1=False
    mult1=False
    div1=True

def eq():
    global product
    global list_num
    global add1
    global sub1
    global mult1
    global div1
    global currentvar

    list_num.append(float(currentvar))

    if(add1==True):
        product=0
        for x in range (0,len(list_num)):
            product=product+list_num[x]
        label1.configure(text=str(product))
        add=False
        list_num.clear()
        currentvar=product

    elif(sub1==True):
        product=list_num[0]
        for x in range (1,len(list_num)):
            product=product-list_num[x]
        label1.configure(text=str(product))
        sub1=False
        list_num.clear()
        currentvar=product

    elif(mult1==True):
        product=1
        for x in range (0,len(list_num)):
            product=product*list_num[x]
        label1.configure(text=str(product))
        mult1=False
        list_num.clear()
        currentvar=product

    elif(div1==True):
        product=list_num[0]
        for x in range (1,len(list_num)):
            product=product/list_num[x]
        label1.configure(text=str(product))
        div1=False
        list_num.clear()
        currentvar=product

def ques():
    print("This button is for testing purposes")
    print(list_num)
    print(product)
    print("Tracer: "+str(tracer))

def clear():
    global currentvar
    global product
    global list_num

    currentvar=""
    product=0
    list_num.clear()
    label1.configure(text="")

root = Tk()
label1=Label(root,text="")
label1.grid(row=0,column=0,columnspan=4)

but7=Button(root,text="7",command=define7)
but7.grid(row=1,column=0)

but8=Button(root,text="8",command=define8)
but8.grid(row=1,column=1,sticky=S)

but9=Button(root,text="9",command=define9)
but9.grid(row=1,column=2,sticky=S)

butdiv=Button(root,text="÷",command=div)
butdiv.grid(row=1,column=3,sticky=S)

but4=Button(root,text="4",command=define4)
but4.grid(row=2,column=0)

but5=Button(root,text="5",command=define5)
but5.grid(row=2,column=1,sticky=S)

but6=Button(root,text="6",command=define6)
but6.grid(row=2,column=2,sticky=S)

butmult=Button(root,text="X",command=mult)
butmult.grid(row=2,column=3,sticky=S)

but1=Button(root,text="1",command=define1)
but1.grid(row=3,column=0)

but2=Button(root,text="2",command=define2)
but2.grid(row=3,column=1,sticky=S)

but3=Button(root,text="3",command=define3)
but3.grid(row=3,column=2,sticky=S)

butsub=Button(root,text="_",command=sub)
butsub.grid(row=3,column=3,sticky=S)


but0=Button(root,text="0",command=define0)
but0.grid(row=4,column=0)

butdot=Button(root,text=".",command=per)
butdot.grid(row=4,column=1,sticky=S)

butplus=Button(root,text="+",command=add)
butplus.grid(row=4,column=2,sticky=S)

buteq=Button(root,text="=",command=eq)
buteq.grid(row=4,column=3,sticky=S)

butc=Button(root,text="c",command=clear)
butc.grid(row=1,column=4)

butc=Button(root,text="?",command=ques)
butc.grid(row=2,column=4)

root.mainloop()
