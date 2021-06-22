from tkinter import *
import random

window = Tk()
window.geometry("800x500")
window.title("DICE ROLLER")

l1 = Label(window, font=("Helvetica", 250))


def roll():
    # to use unicode dice uncomment the below line
    #dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice = [1, 2, 3, 4, 5, 6]
    l1.configure(text=f'{random.choice(dice)} : {random.choice(dice)}')
    l1.pack()


b1 = Button(window, text="Roll", foreground='blue', command=roll)
b1.pack()

window.mainloop()
