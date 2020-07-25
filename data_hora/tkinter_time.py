from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio")


def time():
    string = strftime('%H:%M:%S %p')
    Label.config(Text=string)
    Label.after(1000, time)


label = Label(root, font=("Arial", 80), background="black", foreground="cyan")

label.pack(ANCHOR='center')
time()

mainloop()
