from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.crairBotoes()
        self.criarLabels()
        self.criarCaixaEntrada()

    def crairBotoes(self):
        """
        Criar Botões
        """
        self.botao = Button(self)
        self.botao["text"] = "Python Osso"
        self.botao["fg"] = "red"
        self.botao["bg"] = "yellow"
        self.botao["font"] = ("Arial", "16", "italic", "bold")
        self.botao["height"] = 3
        self.botao["width"] = 30
        self.botao['command'] = self.acaoImprimirPrompt
        self.botao.pack(side="top")

        # Segunda forma de criar botão
        self.botao1 = Button(self, text="Botão no Python",
                             fg="yellow", bg="black")
        self.botao1.pack(side="top")

        # Botão SAIR
        self.sair = Button(self, text="Fechar programa",
                           fg="black", bg="orange", command=root.destroy)
        self.sair.pack(side="top")

    def criarLabels(self):
        self.label = Label(self)
        self.label["text"] = "Aqui é uma Label"
        self.label["font"] = ("Arial", "26", "italic", "bold")
        self.label.pack(side="top")

    def criarCaixaEntrada(self):
        self.editNome = Entry(self)
        self.editNome.pack(side="top")

    def acaoImprimirPrompt(self):
        print("Entry:",self.editNome.get())
        messagebox.showinfo("Nome", self.editNome.get())

root = Tk()

# Criando a aplicação
minha_aplicacao = App(master=root)

minha_aplicacao.master.title("Exempplo de TKinter")

# Tamanho tela
minha_aplicacao.master.geometry("500x300")

# O maximo que pode redimencionar a Janela
minha_aplicacao.master.maxsize(600, 300)

# Inicia a aplicação
minha_aplicacao.mainloop()
