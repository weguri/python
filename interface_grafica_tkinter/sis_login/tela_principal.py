from include.conexao import ConexaoDB
from tkinter import *
from tkinter import messagebox


class TelaPrincipal:
    def __init__(self, master):
        self.frameTop = Frame(master)
        self.frameTop.pack()

        self.exibirMenu(master)
        self.conteudo(master)

    # Exibir o menu
    def exibirMenu(self, master):
        self.menu = Menu(master)

        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(
            label="Cliente", command=self.cadastraCliente)
        self.menuCadastro.add_command(label="Produto")
        self.menuCadastro.add_command(label="Estoque")
        self.menuCadastro.add_command(label="Sair", command=master.destroy)

        # Add ao menu
        self.menu.add_cascade(label="Cadastro", menu=self.menuCadastro)

        # Montar menu Consulta
        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label="Cliente")
        self.menuConsulta.add_command(label="Fornecedores")
        self.menuConsulta.add_command(label="Estoque")

        # Add
        self.menu.add_cascade(label="Consulta", menu=self.menuConsulta)

        master.config(menu=self.menu)

    # Conteudo no Frame
    def conteudo(self, master):
        frameMid = Frame(master)
        Label(frameMid, text="Lista de Pessoas", font=("Arial", 15)).grid(
            row=1, column=1, columnspan=4, pady=5)
        Label(frameMid, text="Código", relief=RIDGE, width=7,
              bg="dark grey").grid(row=2, column=1)
        Label(frameMid, text="Nome", relief=RIDGE, width=30,
              bg="dark grey").grid(row=2, column=2)
        Label(frameMid, text="Telefone", relief=RIDGE, width=15,
              bg="dark grey").grid(row=2, column=3)
        Label(frameMid, text="E-mail", relief=RIDGE, width=30,
              bg="dark grey").grid(row=2, column=4)

        try:
            conn = ConexaoDB().conexao()
            cursor = conn.cursor(buffered=True, raw=True)

            sql = """ select 
                            id_clientes, nome_clientes, telefone_clientes, email_clientes
                        from clientes order by id_clientes asc limit 10; """

            cursor.execute(sql)

            contRow = 2
            for (codigo, nome, fone, email) in cursor:

                # print(codigo.decode(), nome.decode(), fone.decode(), email.decode())

                corRow = "white" if contRow % 2 == 0 else "light gray"

                Label(frameMid, text=codigo.decode(), relief=RIDGE, width=7,
                      bg=corRow).grid(row=contRow + 1, column=1)

                Label(frameMid, text=nome.decode(), relief=RIDGE, width=30, bg=corRow,
                      anchor=W).grid(row=contRow + 1, column=2)

                Label(frameMid, text=fone.decode(), relief=RIDGE, width=15, bg=corRow).grid(
                    row=contRow + 1, column=3)

                Label(frameMid, text=email.decode(), relief=RIDGE, width=30,
                      bg=corRow, anchor=E).grid(row=contRow + 1, column=4)

                contRow += 1

        except Exception as err:
            print("Erro:", err)
        else:
            cursor.close()
            conn.close()

        frameMid.pack()

    # Exibir lista

    def cadastraCliente(self):
        print("Clicou cliente")


def abrirSistemaPrincipal():
    """ 
    Carregar a tela principal
    """
    root = Tk()
    TelaPrincipal(root)
    root.geometry("680x350+350+80")
    root.title("Sistema de estoque")
    root.mainloop()

# abrirSistemaPrincipal()
