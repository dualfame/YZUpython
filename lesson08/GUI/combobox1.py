import tkinter
from tkinter import ttk
from tkinter import messagebox

def submit():
    messagebox.showinfo('結帳', "{0}".format(combo1.get()))

win = tkinter.Tk()
win.geometry('600x200')

fruits = ['apple', 'banana', 'lemon', 'mango', 'watermelon']
drinks = {'紅茶':50, '青茶':50, '鮮奶':75}

label1 = tkinter.Label(win, text="品項")
combo1 = ttk.Combobox(win, values=list(drinks.keys()), state='readonly')

label2 = tkinter.Label(win, text="甜度")
rdio1 = tkinter.Radiobutton(win, text='全糖', value=1.0)
rdio2 = tkinter.Radiobutton(win, text='半糖', value=0.5)
rdio3 = tkinter.Radiobutton(win, text='無糖', value=0)

label3 = tkinter.Label(win, text="額外需求")
chk1 = tkinter.Checkbutton(win, text="去冰")
chk2 = tkinter.Checkbutton(win, text="塑膠袋")

btn = tkinter.Button(win, text="結帳", command=submit)

#版面
label1.grid(column=0, row=1, padx=0, pady=10, sticky="W")
combo1.grid(column=0, row=1, padx=50, pady=10, sticky="W")
label2.grid(column=0, row=2, padx=0, pady=10, sticky="W")
rdio1.grid(column=0, row=2, padx=50, pady=10, sticky="W")
rdio2.grid(column=0, row=2, padx=100, pady=10, sticky="W")
rdio3.grid(column=0, row=2, padx=150, pady=10, sticky="W")
label3.grid(column=0, row=3, padx=0, pady=10, sticky="W")
chk1.grid(column=0, row=3, padx=50, pady=10, sticky="W")
chk2.grid(column=0, row=3, padx=100, pady=10, sticky="W")
btn.grid(column=0, row=4, padx=0, pady=10, sticky="W")

win.mainloop()
