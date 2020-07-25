from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.btnNumericoCalc()

    def btnNumericoCalc(self):
        self.edit = Entry(self.master)
        self.edit.grid(row=1, column=0)

        botoes = ["7", "8", "9", "/", "4", "5", "6",
                  "*", "1", "2", "3", "-", "0", "CE", "+", "="]

        linha = 1
        coluna = 1

        for btn in botoes:
            def comando(x=btn): return self.calcular(x)
            self.botao = Button(self, text=btn, height="1", width="2",
                                fg="black", bg="dark grey", command=comando).grid(row=linha, column=coluna)
            coluna += 1
            if coluna > 4:
                linha += 1
                coluna = 1

    def calcular(self, valorBtn):
        if valorBtn == "=":
            try:
                calculo = eval(self.edit.get())
                self.edit.insert(END, "=" + str(calculo))
            except:
                self.edit.insert(END, " = ERRO")
        elif valorBtn == "CE":
            self.edit.delete(0, END)
        else:
            if "=" in self.edit.get():
                self.edit.delete(0, END)
                
            self.edit.insert(END, valorBtn)



root = Tk()

# Criando a aplicação
minha_aplicacao = App(master=root)

minha_aplicacao.master.title("Calc")

# Tamanho tela
# minha_aplicacao.master.geometry("500x300")

# O maximo que pode redimencionar a Janela
minha_aplicacao.master.maxsize(178, 150)

minha_aplicacao.master.minsize(178, 150)

# Inicia a aplicação
minha_aplicacao.mainloop()
