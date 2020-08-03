from tkinter import *

root = Tk()

labelTitulo = Label(text="Exemplos de Tkinter", padx=10).pack(side=LEFT)
imagem = PhotoImage(file="ubuntu.png")
labelImagem = Label(root, image=imagem).pack(side=RIGHT)

root.mainloop()