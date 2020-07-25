def ListarClientes(conn, opcao):

    strSql = "select * from clientes"
    if opcao == 4:
        pesquisar = input("Digite nome a pesquisar: ")
        strSql += " where nome_clientes like '%"+pesquisar+"%';"
    
    c = conn.cursor(prepared=True)
    try:
        c.execute(strSql)
        dadosCliente = c.fetchall()

        print("\n", '-' * 63, "\n", '-'*22,
              'Lista de Clientes', '-'*22, "\n", '-' * 63, "\n")

        for d in dadosCliente:
            codigo = d[0]
            nome = d[1]
            fone = d[2]
            email = d[3]

            print(
                "Código: {0}, Nome: {1}, Fone: {2}, E-mail: {3}".format(codigo, nome, fone, email))

        print()
        print("Total registros: %d\n\n" % c.rowcount)
        input("")
    except:
        raise Exception("Erro, para listar todos os clientes.")
    finally:
        c.close()
        conn.close()
