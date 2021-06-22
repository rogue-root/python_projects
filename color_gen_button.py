import random
from tkinter import *

# to make a rgb value

window = Tk()
l = Label(window, font=("Helvetica", 50))


def col_gen():
    r = random.randint(10, 255)
    b = random.randint(10, 255)
    g = random.randint(10, 255)
    print("the rgb value is: ", r, b, g)

    r_hex = hex(r)
    b_hex = hex(b)
    g_hex = hex(g)
    hexa = ('#'+str(r_hex)+str(b_hex)+str(g_hex))
    rgb_hex = hexa.replace('0x', '')
    l.configure(text=f'generated colour: \n {rgb_hex}', background=rgb_hex)
    l.pack()
    window.config(background=rgb_hex)
    print("the hexadecimal value is: ", rgb_hex)
    return rgb_hex


window.title("random color")
window.geometry("800x300")

b1 = Button(window, text="Random Color", foreground='blue', command=col_gen)
b1.pack()

window.mainloop()
