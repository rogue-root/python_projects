from tkinter import *

with open("sample.txt", "rt") as f:
    data = f.read()
    words = data.split()

print("number of words: ", len(words))

window = Tk()
window.title("Word Counter")
window.geometry("600x300")
window.config(background="#7e6089")

var = StringVar()
var.set("Total Words :\n "+str(len(words)))

l2 = Label(window, textvariable=var, font=(
    "arial", 50), bg="#7e6089", justify=CENTER)
l2.pack()

window.mainloop()
