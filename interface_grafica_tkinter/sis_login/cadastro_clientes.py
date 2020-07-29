import mysql.connector
from include.conexao import ConexaoDB
from tkinter import *


""" 
Sistema para gerenciar - Clientes
    Cadastra
    Alterar
    Excluir
    Pesquisar
"""


def cadastraCliente():
    """ 
    Cadastrar novo cliente
    """
    nome = editNome.get()
    fone = editFone.get()
    email = editEmail.get()
    if nome == "" or fone == "" or email == "":
        labelStatus["text"] = "Todos campos são obrigatório"
    else:
        try:
            conn = ConexaoDB().conexao()
            c = conn.cursor(prepared=True)

            dados = [(nome, fone, email)]

            # Mondar SQL
            strSQL = """ INSERT INTO clientes 
                            (nome_clientes, telefone_clientes, email_clientes, aniversario) 
                        VALUES (%s, %s, %s, NOW()); """
            
            c.executemany(strSQL, dados)
            conn.commit()
            labelStatus["text"] = "Gravado com sucesso!"

        #
        # Except de varios erros
        except (mysql.connector.IntegrityError, mysql.connector.DataError) as err:
            print("IntegrityError or DataError")
            print(err)

        except mysql.connector.ProgrammingError as err:
            print("ProgrammingError")
            print(err.errno)
            print(err.sqlstate)
            print(err.msg)

        except mysql.connector.Error as err:
            print("Error")
            print(err)
        else:
            novoCliente()
            c.close()
            conn.close()


def novoCliente():
    """ 
    Para limpar as caixa de Texto
    """
    editCodigo.configure(state="normal") # Para desbloquear a caixa de texto
    editCodigo.delete(0, END)
    editCodigo.configure(state="readonly")

    editNome.delete(0, END)
    editFone.delete(0, END)
    editEmail.delete(0, END)
    editNome.focus()


def pesquisarCliente():
    """
    Pesquisar pelo nome do cliente
    """
    # Valor a ser pesquisado
    pesquisar = editpesquisa.get()

    try:
        # Conexção ao Banco de dados
        conn = ConexaoDB(True).conexao()

        # tupla nomeada com buffer.
        cursor = conn.cursor(named_tuple=True)

        # Montar SQL
        cursor.execute("SELECT id_clientes, nome_clientes, telefone_clientes, email_clientes "
                        "FROM clientes "
                        "WHERE nome_clientes LIKE %s LIMIT %s;", (f"%{pesquisar}%", 1,))
        
        if cursor.rowcount > 0:
            # Limpar Campos
            labelStatus["text"] = ""
            novoCliente()
        else:
            labelStatus["text"] = "Não existe"

        for row in cursor:
            editCodigo.configure(state="normal")
            editCodigo.insert(0, row.id_clientes)
            editCodigo.configure(state="readonly")

            editNome.insert(0, row.nome_clientes)
            editFone.insert(0, row.telefone_clientes)
            editEmail.insert(0, row.email_clientes)


    except Exception as err:
        labelStatus["text"] = "Ocorreu um erro, desculpe"
        print(err)
    else:
        cursor.close()
        conn.close()


def excluirCliente():
    codigo = editCodigo.get()
    try:
        if codigo == "":
            raise Exception("Faça uma pesquisa")

        conn = ConexaoDB().conexao()
        cursor = conn.cursor()
        sql = """ DELETE FROM clientes WHERE id_clientes = %s; """
        val = (codigo,)
        cursor.execute(sql, val)
        conn.commit()

        labelStatus["text"] = "registro deletado."
        
        editpesquisa.delete(0, END)

        # Limpar Campos
        pesquisarCliente()

    except Exception as err:
        labelStatus["text"] = err
        print(err)
    else:
        cursor.close()
        conn.close()


def alterarCliente():
    try:
        conn = ConexaoDB().conexao()
        cursor = conn.cursor()

        sql = """ UPDATE 
                clientes 
            SET 
                nome_clientes = %(nome)s,
                telefone_clientes = %(fone)s, 
                email_clientes = %(email)s 
            WHERE 
                id_clientes = %(id)s; """
        
        data_list = [
            {
                'nome': editNome.get(),
                'fone': editFone.get(),
                'email': editEmail.get(),
                'id': editCodigo.get()
            },
        ]

        cursor.executemany(sql, data_list)
        conn.commit()

        labelStatus["text"] = "Registro atualizado."

    except Exception as err:
        labelStatus["text"] = err
    else:
        cursor.close()
        conn.close()


""" 

Montar Tela de gerenciamento de cliente

"""

formeClientes = Tk()
formeClientes.title("Cadastro de Clientes")

# 450x300 -> lagura por altura
# +500+200 -> posição na tela
formeClientes.geometry("480x330+500+200")

titulo = Label(formeClientes, text="Cadastro")
titulo.grid(row=0, sticky=W+E+N+S, pady=5, padx=5)

#
# Linha para dividir o frame
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=1, pady=5, stick=W+E+N+S, columnspan=4)

#
# Pesquisa
labelpesquisa = Label(formeClientes, text="Pesquisar.:")
labelpesquisa.grid(row=2, column=0, stick=W+E+N+S, pady=5, padx=5)

editpesquisa = Entry()
editpesquisa.grid(row=2, column=1, stick=W+E+N+S)

btnPesquisa = Button(formeClientes, text="Pesquisar", command=pesquisarCliente)
btnPesquisa.grid(row=2, column=3, padx=5)

#
# Linha para dividir o frame
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=3, pady=10, stick=W+E+N+S, columnspan=4)

#
# Labels para exibir na tela
labelCodigo = Label(formeClientes, text="Código..:")  # , anchor=E
labelNome = Label(formeClientes, text="Nome..:")  # , anchor=E
labelFone = Label(formeClientes, text="Fone..:")  # , anchor=E
labelEmail = Label(formeClientes, text="Email.:")  # , anchor=E
labelStatus = Label(formeClientes, text="Status")

#
# Caixa de Entrada(input)
editCodigo = Entry(state="readonly")
editNome = Entry()
editFone = Entry()
editEmail = Entry()

#
# Posicionamento no formulário dos Labels e Edits de Pessoas
labelCodigo.grid(row=4, sticky=W+E+N+S, padx=10)
editCodigo.grid(row=4, column=1, sticky=W+E+N+S)

labelNome.grid(row=5, sticky=W+E+N+S, padx=10)
editNome.grid(row=5, column=1, sticky=W+E+N+S)

labelFone.grid(row=6, sticky=W+E+N+S, padx=10)
editFone.grid(row=6, column=1, sticky=W+E+N+S)

labelEmail.grid(row=7, sticky=W+E+N+S, padx=10)
editEmail.grid(row=7, column=1, sticky=W+E+N+S)

#
# Painel de Botões, para gerenciar Clientes
frameBotao = Frame()
botaoNovo = Button(frameBotao, text="Novo", command=novoCliente)
botaoGravar = Button(frameBotao, text="Gravar", command=cadastraCliente)
botaoAlterar = Button(frameBotao, text="Alterar", command=alterarCliente)
botaoExcluir = Button(frameBotao, text="Excluir", command=excluirCliente)

#
# Posicionar dentro do frame frameBotao
botaoNovo.grid(row=1, column=0, pady=10, padx=2)
botaoGravar.grid(row=1, column=1, pady=10, padx=2)
botaoAlterar.grid(row=1, column=2, pady=10, padx=2)
botaoExcluir.grid(row=1, column=3, pady=10, padx=2)

#
# posicionar o frameBotao dentro do formePessoas
frameBotao.grid(row=8, column=1)

#
# Exibir o status
labelStatus.grid(row=9, column=1, pady=10)

# 
# Carrega o primeiro do MySQL
pesquisarCliente()

mainloop()
