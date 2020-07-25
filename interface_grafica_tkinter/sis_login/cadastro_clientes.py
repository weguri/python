from interface_grafica_tkinter.sis_login.conexao import ConexaoDB
from tkinter import *


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
                            (nome_clientes, telefone_clientes, email_clientes) 
                        VALUES (%s, %s, %s); """
            try:
                c.executemany(strSQL, dados)
                conn.commit()
                labelStatus["text"] = "Gravado com sucesso!"
                novoCliente()
            except:
                raise Exception("Erro: Não foi possível gravar a informação")
            finally:
                c.close()
                conn.close()

        except Exception as err:
            labelStatus["text"] = err


def novoCliente():
    """ 
    Para limpar as caixa de Texto
    """
    editNome.delete(0, END)
    editFone.delete(0, END)
    editEmail.delete(0, END)
    editNome.focus()


def pesquisarCliente():
    novoCliente()
    pesquisar = editpesquisa.get()
    sql = """ select * from clientes where 
                    nome_clientes like %s limit %s; """
    dados = (f"%{pesquisar}%", 1,)

    try:
        conn = ConexaoDB().conexao()
        c = conn.cursor(prepared=True)
        try:
            c.execute(sql, dados)
            for linha in c:
                editNome.insert(0, linha[1])
                editFone.insert(0, linha[2])
                editEmail.insert(0, linha[3])

        except:
            raise Exception("Erro, para localizar")
        finally:
            c.close()
            conn.close()

    except Exception as err:
        labelStatus["text"] = err


formeClientes = Tk()
formeClientes.title("Cadastro de Clientes")

# 450x300 -> lagura por altura
# +500+200 -> posição na tela
formeClientes.geometry("480x350+500+200")

titulo = Label(formeClientes, text="Cadastro")
titulo.grid(row=0, sticky=W+E+N+S, pady=5, padx=5)

# Linha para dividir o frame
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=1, pady=5, stick=W+E+N+S, columnspan=4)

# Pesquisa
labelpesquisa = Label(formeClientes, text="Pesquisar.:")
labelpesquisa.grid(row=2, column=0, stick=W+E+N+S, pady=5, padx=5)

editpesquisa = Entry()
editpesquisa.grid(row=2, column=1, stick=W+E+N+S)

btnPesquisa = Button(formeClientes, text="Pesquisar", command=pesquisarCliente)
btnPesquisa.grid(row=2, column=3, padx=5)

# Linha para dividir o frame
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=3, pady=10, stick=W+E+N+S, columnspan=4)

# Labels para exibir na tela
labelNome = Label(formeClientes, text="Nome..:")  # , anchor=E
labelFone = Label(formeClientes, text="Fone..:")  # , anchor=E
labelEmail = Label(formeClientes, text="Email.:")  # , anchor=E
labelStatus = Label(formeClientes, text="Status")

# Caixa de Entrada(input)
editNome = Entry()
editFone = Entry()
editEmail = Entry()

# Posicionamento no formulário dos Labels e Edits de Pessoas
labelNome.grid(row=4, sticky=W+E+N+S, padx=10)
editNome.grid(row=4, column=1, sticky=W+E+N+S)

labelFone.grid(row=5, sticky=W+E+N+S, padx=10)
editFone.grid(row=5, column=1, sticky=W+E+N+S)

labelEmail.grid(row=6, sticky=W+E+N+S, padx=10)
editEmail.grid(row=6, column=1, sticky=W+E+N+S)

# Painel de Botões, para gerenciar Clientes
frameBotao = Frame()
botaoNovo = Button(frameBotao, text="Novo", command=novoCliente)
botaoGravar = Button(frameBotao, text="Gravar", command=cadastraCliente)
botaoAlterar = Button(frameBotao, text="Alterar")
botaoExcluir = Button(frameBotao, text="Excluir")

# Posicionar dentro do frame frameBotao
botaoNovo.grid(row=1, column=0, pady=10, padx=2)
botaoGravar.grid(row=1, column=1, pady=10, padx=2)
botaoAlterar.grid(row=1, column=2, pady=10, padx=2)
botaoExcluir.grid(row=1, column=3, pady=10, padx=2)

# posicionar o frameBotao dentro do formePessoas
frameBotao.grid(row=7, column=1)

# Exibir o status
labelStatus.grid(row=8, column=1, pady=10)

mainloop()
