from tkinter import *
from PIL import ImageTK, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

frame = LabelFrame(root, text="This is my Frame ...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b.pack(row=0, column=0)

root.mainloop()