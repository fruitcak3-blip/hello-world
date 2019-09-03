from tkinter import *
from random import *
def callback():
     label1=Label(root,text=str(randint(1,10)))
     label1.pack()
root=Tk()
b = Button(root, text="OK", command=callback)
b.pack()
root.mainloop()
