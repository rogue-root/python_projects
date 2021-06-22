# program to generate a 10 digit password

import random
from tkinter import *


window = Tk()
window.title("Password generator")
window.geometry("800x300")
window.config(background="#f99db7")
l1 = Label(window, font=("Helvetica", 50), background="#f99db7")


def passwordd():
    d1 = chr(random.randint(65, 90))  # generate upper case letter
    d2 = chr(random.randint(65, 90))
    d3 = chr(random.randint(65, 90))
    d4 = chr(random.randint(97, 122))  # generate lower case letter
    d5 = chr(random.randint(97, 122))
    d6 = chr(random.randint(33, 64))  # generate special character
    d7 = chr(random.randint(33, 64))
    d8 = chr(random.randint(48, 57))  # generate numbers
    d9 = chr(random.randint(48, 57))
    d10 = chr(random.randint(48, 57))

    digit = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
    password = ""

    # shuffle the digits
    random.shuffle(digit)
    p = password.join(digit)
    print("The generated password is: ", p)
    l1.configure(text=f'password:\n {p}')
    l1.pack()


b1 = Button(window, text="generate", foreground='blue', command=passwordd)
b1.pack()

window.mainloop()
