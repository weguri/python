from tkinter import *
from tkinter import messagebox

class TelaPrincipal:
    def __init__(self, master):
        self.frameTop = Frame(master)
        self.frameTop.pack()

        self.exibirMenu(master)

        self.frameMid = Frame(master)
        botaoNovo = Button(self.frameMid, text="Novo")
        botaoNovo.grid(row=1, column=0, pady=10, padx=2)
        self.frameMid.pack()
 
    # Exibir o menu
    def exibirMenu(self, master):
        self.menu = Menu(master)

        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(
            label="Cliente", command=self.cadastraCliente)
        self.menuCadastro.add_command(label="Produto")
        self.menuCadastro.add_command(label="Estoque")
        self.menuCadastro.add_command(label="Sair", command=master.destroy)
        self.menu.add_cascade(label="Cadastro", menu=self.menuCadastro)

        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label="Cliente")
        self.menuConsulta.add_command(label="Fornecedores")
        self.menuConsulta.add_command(label="Estoque")
        self.menu.add_cascade(label="Consulta", menu=self.menuConsulta)

        master.config(menu=self.menu)

    # Exibir lista
    def cadastraCliente(self):
        print("Clicou cliente")

# Carregar
# Abrir a tela principal
def abrirSistemaPrincipal():
    root = Tk()
    TelaPrincipal(root)
    root.geometry("480x350+500+200")
    root.title("Sistema de estoque")
    root.mainloop()

# root = Tk()
# TelaPrincipal(root)
# root.geometry("480x350+500+200")
# root.title("Sistema de estoque")
# root.mainloop()