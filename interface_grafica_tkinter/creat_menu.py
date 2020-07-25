from tkinter import *
from tkinter import messagebox

class Sistema:
    def __init__(self, master):
        self.frame = Frame(master)
        self.master = master
        self.frame.pack()
        
        self.menu = Menu(master)

        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(
            label="Cliente", command=self.cadastraCliente)
        self.menuCadastro.add_command(label="Produto")
        self.menuCadastro.add_command(label="Estoque")
        self.menuCadastro.add_command(label="Sair", command=self.master.destroy)
        self.menu.add_cascade(label="Cadastro", menu=self.menuCadastro)

        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label="Cliente")
        self.menuConsulta.add_command(label="Fornecedores")
        self.menuConsulta.add_command(label="Estoque")
        self.menu.add_cascade(label="Consulta", menu=self.menuConsulta)

        master.config(menu=self.menu)

    def cadastraCliente(self):
        print("Clicou cliente")


def sair():
    if messagebox.askyesno("Fechar Janela", "Tem certeza"):
        exit()
    else:
        pass

root = Tk()
root.protocol("WM_DELETE_WINDOW", sair)
root.geometry("300x200")
root.title("Sistema de estoque")
Sistema(root)
root.mainloop()
