from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.criarBotoes()

    def criarBotoes(self):
        self.btn1 = Button(self, text="1º Btn", fg="yellow", bg="black")
        self.btn1.pack(side="top")

        self.btn2 = Button(self, text="2º Btn", fg="yellow", bg="black")
        self.btn2.pack(side="top")

        self.btn3 = Button(self, text="3º Btn", fg="yellow", bg="black")
        self.btn3.pack(side="left")

        self.btn4 = Button(self, text="4º Btn", fg="yellow", bg="black")
        self.btn4.pack(side="right")

        self.btn5 = Button(self, text="5º Btn", fg="yellow", bg="black")
        self.btn5.pack(side="bottom")


root = Tk()

# Criando a aplicação
minha_aplicacao = App(master=root)

minha_aplicacao.master.title("Posicionamento TKinter")

# Tamanho tela
minha_aplicacao.master.geometry("500x300")

# O maximo que pode redimencionar a Janela
minha_aplicacao.master.maxsize(600, 300)

# Inicia a aplicação
minha_aplicacao.mainloop()
