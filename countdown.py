from tkinter import *
import time

# window = Tk()
# window.title("CountDown")
# window.geometry("600x300")
# l = Label(window, font=("Helvetica", 50))


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        # l.configure(text=f'countdown: \n {timer}')
        # l.pack()
    print('Your time is up!')


# input time in seconds
t = input("Enter the time in seconds: ")
# function call
countdown(int(t))


# window.config(background="#7e6089")
# b1 = Button(window, text="start",
#             foreground='blue', command=countdown)
# b1.pack()
# window.mainloop()
