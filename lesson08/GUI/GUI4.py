import tkinter

def myadd():
    num.set(num.get() + 1)

win = tkinter.Tk()
win.geometry('200x200')

num = tkinter.IntVar()
num.set(0)

label = tkinter.Label(win, textvariable=num)
label.pack()
buttom = tkinter.Button(win, text="ADD", command=myadd)
buttom.pack()

win.mainloop()