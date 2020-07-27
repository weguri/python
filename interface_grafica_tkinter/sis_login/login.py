from interface_grafica_tkinter.sis_login.tela_principal import abrirSistemaPrincipal
from tkinter import messagebox
from include.conexao import ConexaoDB
import sys
from tkinter import Button, Entry, Label


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Acesso ao sistema")
        Label(self.master, text="Usuario e Senha").grid(
            row=1, column=1, columnspan=2, pady=4)

        Label(self.master, text="Usuario:").grid(row=2, column=1, pady=2)
        self.usuario = Entry(self.master, font=("Windings", "10"))
        self.usuario.grid(row=2, column=2)
        self.usuario.focus_force()

        Label(self.master, text="Senha:").grid(row=3, column=1, pady=2)
        self.senha = Entry(self.master, show="*", fg="darkgrey")
        self.senha.grid(row=3, column=2)

        self.status = Label(self.master, text="Status....")
        self.status.grid(row=4, column=1, columnspan=2, pady=4)

        self.btn_entrar = Button(self.master, width=7,
                                 text="Entrar", command=self.validarEntrada)
        self.btn_entrar.grid(row=1, column=3, padx=4, rowspan=2)

        self.btn_sair = Button(self.master, width=7,
                               text="Sair", command=master.destroy)
        self.btn_sair.grid(row=3, column=3, rowspan=2)

    """
    Validar os dados de acesso ao sistema
    """

    def validarEntrada(self):
        u = self.usuario.get()
        s = self.senha.get()
        try:
            cn = ConexaoDB()
            conn = cn.conexao()
            c = conn.cursor()

            sql = """ select id_login from login where 
                        user_login = %(usuario)s and password_login = %(senha)s; """
            dados = {'usuario': u, 'senha': s}

            c.execute(sql, dados)
            c.fetchone()
            if c.rowcount == 1:
                self.status['text'] = "Acesso Aprovado"
                self.master.destroy()
                abrirSistemaPrincipal()
            else:
                self.status['text'] = "Login ou senha inválido."

            conn.close()
        except Exception as err:
            messagebox.showwarning("Error", err)

    def sairSistema(self):
        sys.exit(1)
