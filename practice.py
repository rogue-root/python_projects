from tkinter import *

x = 'hey'
window = Tk()
window.geometry("300x300")
var = StringVar()
var.set(x)

l = Label(window, textvariable=var)
l.pack()
window.mainloop()
