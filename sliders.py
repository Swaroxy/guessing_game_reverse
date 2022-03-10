from tkinter import *
from PIL import ImageTk,Image
# from tkinter import filedialog

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:')
root.geometry("")

vertical = Scale(root, from_= 0, to=200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()