from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.btnNumericoCalc()

    def btnNumericoCalc(self):
        # Linha Um
        self.btn7 = Button(self, text="7", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="1", column="1")
        self.btn8 = Button(self, text="8", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="1", column="2")
        self.btn9 = Button(self, text="9", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="1", column="3")
        self.btndiv = Button(self, text="/", height="1", width="2",
                             fg="black", bg="dark grey").grid(row="1", column="4")

        # Linha 2
        self.btn4 = Button(self, text="4", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="2", column="1")
        self.btn5 = Button(self, text="5", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="2", column="2")
        self.btn6 = Button(self, text="6", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="2", column="3")
        self.btnmult = Button(self, text="*", height="1", width="2",
                              fg="black", bg="dark grey").grid(row="2", column="4")

        # Linha 3
        self.btn1 = Button(self, text="1", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="3", column="1")
        self.btn2 = Button(self, text="2", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="3", column="2")
        self.btn3 = Button(self, text="3", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="3", column="3")
        self.btnmenos = Button(self, text="-", height="1", width="2",
                               fg="black", bg="dark grey").grid(row="3", column="4")

        # Linha 4
        self.btn0 = Button(self, text="0", height="1", width="2",
                           fg="black", bg="dark grey").grid(row="4", column="1")
        self.btnzerar = Button(self, text="CE", height="1", width="2",
                               fg="black", bg="dark grey").grid(row="4", column="2")
        self.btnsoma = Button(self, text="+", height="1", width="2",
                              fg="black", bg="dark grey").grid(row="4", column="3")
        self.btnigual = Button(self, text="=", height="1", width="2",
                               fg="black", bg="dark grey").grid(row="4", column="4")


root = Tk()

# Criando a aplicação
minha_aplicacao = App(master=root)

minha_aplicacao.master.title("Calculadora TKinter")

# Tamanho tela
# minha_aplicacao.master.geometry("500x300")

# O maximo que pode redimencionar a Janela
minha_aplicacao.master.maxsize(600, 300)

# Inicia a aplicação
minha_aplicacao.mainloop()
