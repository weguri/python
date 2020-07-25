
def Cadastro(conn):

    print("\n", '-' * 61, "\n", '-'*22,
          'Cadastro de Pessoas', '-'*22, "\n", '-' * 61, "\n")

    nome = input("Nome.: ")
    fone = input("Telefone.: ")
    email = input("E-mail.: ")

    dados = [(nome, fone, email)]

    # Mondar SQL
    strSQL = "INSERT INTO clientes "\
        "(nome_clientes, telefone_clientes, email_clientes) "\
        "VALUES (%s, %s, %s);"

    c = conn.cursor(prepared=True)
    try:
        c.executemany(strSQL, dados)
        conn.commit()

        print("\nTotal: {0} Registros gravados\n".format(c.rowcount))
        print("Gravado com suceeso!\n\n")
    except:
        raise Exception("Erro: Não foi possível gravar a informação")
    finally:
        c.close()
        conn.close()
