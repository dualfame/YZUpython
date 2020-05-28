import tkinter
from tkinter import messagebox

def mymessage():
    messagebox.showinfo('Message', 'HELLO')

def exit():
    win.quit()

win = tkinter.Tk()

buttom = tkinter.Button(win, text="OK!", command=mymessage)
buttom.pack()
buttom2 = tkinter.Button(win, text="EXIT", command=exit)
buttom2.pack()

win.geometry('300x300')
win.mainloop()