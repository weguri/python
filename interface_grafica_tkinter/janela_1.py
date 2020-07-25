from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry("290x100")
tk.title("Exemplo de Window")


def clique_aqui():
    messagebox.showinfo("Curso de Pythone", "Seja aqui")


btn = Button(tk, text="Clique aqui", command=clique_aqui)
btn.place(x=50, y=50)

tk.mainloop()
