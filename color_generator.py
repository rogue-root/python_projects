import random
from tkinter import *

# to make a rgb value


r = random.randint(10, 255)
b = random.randint(10, 255)
g = random.randint(10, 255)
print("the rgb value is: ", r, b, g)

r_hex = hex(r)
b_hex = hex(b)
g_hex = hex(g)
hexa = ('#'+str(r_hex)+str(b_hex)+str(g_hex))
rgb_hex = hexa.replace('0x', '')
print("the hexadecimal value is: ", rgb_hex)


window = Tk()
window.title("random color")
window.geometry("800x300")
window.config(background=rgb_hex)
var = StringVar()
var.set("Hexa Color Code: \n"+rgb_hex)

l = Label(window, textvariable=var,
          font=("Helvetica", 50), bg=rgb_hex, justify=CENTER)
l.pack()
window.mainloop()
