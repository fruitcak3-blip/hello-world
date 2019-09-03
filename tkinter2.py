from tkinter import *
from random import *
from time import sleep

colors=["red","blue","black","green","yellow"]

def callback():

    test=Label(root,text="THIS IS A TEST",bg="white",fg=colors[randint(0,4)])
    test.pack()
    sleep(1)
    test.destroy()


root=Tk()

b = Button(root, text="OK", command=callback)
b.pack()


root.mainloop()
