from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Codemy.com - Learn to Code!')
root.iconbitmap('C:')
root.geometry("")

def show():
    myLabel = Label(root, text=clicked.get().pack())

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
drop.pack()

myButton = Button(root, text="Show Selection", command=show)

root.mainloop()