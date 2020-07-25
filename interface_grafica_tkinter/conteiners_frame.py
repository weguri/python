from tkinter import *


class Conteiners:
    def __init__(self, master):
        self.conteinerTop = Frame(master)
        self.conteinerMeio = Frame(master)
        self.conteinerBaixo = Frame(master)
        self.conteinerSeparar = Frame(height=3, width=200, bd=2, relief=SUNKEN)

        self.conteinerTop.pack()
        self.conteinerSeparar.pack()
        self.conteinerMeio.pack()
        self.conteinerSeparar.pack()
        self.conteinerBaixo.pack()

        Button(self.conteinerTop, text="Botão 1").pack()
        Button(self.conteinerMeio, text="Botão 2").pack(side=LEFT)
        Button(self.conteinerMeio, text="Botão 3").pack(side=RIGHT)
        Button(self.conteinerBaixo, text="Fechar Janela",
               command=self.fechar).pack()

    def fechar(self):
        exit()


def sair():
    pass

root = Tk()
root.protocol("WM_DELETE_WINDOW", sair)
tela = Conteiners(root)
tela.geometry("340x120")
root.mainloop()
