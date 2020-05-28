import tkinter

win = tkinter.Tk()

win.title('My Windows')
label = tkinter.Label(win, text="HELLO")
label.pack(side=tkinter.LEFT)
win.geometry('300x300')
win.mainloop()
