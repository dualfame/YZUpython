import tkinter

win = tkinter.Tk()

win.title('My Windows')
label1 = tkinter.Label(win, text="HELLO1", bg="red")
label2 = tkinter.Label(win, text="HELLO2")
label3 = tkinter.Label(win, text="HELLO3", font='16', fg='blue')
label4 = tkinter.Label(win, text="HELLO4")
label5 = tkinter.Label(win, text="HELLO5")
button = tkinter.Button(win, text="CLICK", font=('calibri', 20))
label1.grid(column=0, row=0)
label2.grid(column=1, row=1, padx=10, pady=10)  #padx,y : 留邊
label3.grid(column=3, row=1)
label4.grid(column=3, row=3)
label5.grid(column=9, row=9)
button.grid(column=5, row=5)
win.geometry('300x300')
win.mainloop()
