import tkinter
from tkinter import messagebox
def mytext():
    messagebox.showinfo("message", entry.get())

win = tkinter.Tk()
win.geometry('200x200')

num = tkinter.IntVar()
num.set(0)

entry = tkinter.Entry(win, justify=tkinter.CENTER)
entry.pack()

buttom = tkinter.Button(win, text="GET", command=mytext)
buttom.pack()

win.mainloop()