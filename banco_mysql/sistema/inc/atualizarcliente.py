def AtualizarCliente(conn):
    print("\n", '-' * 63, "\n", '-'*22,
          'Atualizar Clientes', '-'*22, "\n", '-' * 63, "\n")

    print("Informe os dados abaixo para atualizar")
    id = int(input("código: "))
    nome = input("Nome: ")
    fone = input("Telefone: ")
    email = input("E-mail: ")

    sql = ("UPDATE clientes SET "
           "nome_clientes='%s', "
           "telefone_clientes='%s', "
           "email_clientes='%s' "
           "WHERE id_clientes = %d;" % (nome, fone, email, id))

    c = conn.cursor()
    try:
        c.execute(sql)
        conn.commit()

        if c.rowcount > 0:
            print("\nCódigo: %d, atualizado com sucesso" % id)
        else:
            print("Nenhum registro foi atualizado!")

        input("")
    except:
        raise Exception("Erro, Não foi possivel atualizar.")
    finally:
        c.close()
        conn.close()
