from tkinter import *
from PIL import ImageTK,Image
from tkinter import messagebox

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

r = IntVar()
r.set("2")

TOPPINGS = [
    ("Peperonni", "Peperonni")
    ("Cheese", "Cheese")
    ("Mushroom", "Mushroom")
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Peperoni")

for text, toipping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=r.value)
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked()).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked()).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()
mainloop()