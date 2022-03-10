from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('C:')


def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap('C:')
    my_img = ImageTk.PhotoImage(Image.open("Pictures\ppcf2"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()

mainloop() 