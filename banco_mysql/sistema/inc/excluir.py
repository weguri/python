def Excluir(conn):
    print("\n", '-' * 63, "\n", '-'*22,
          'Excluir Clientes', '-'*22, "\n", '-' * 63, "\n")

    idEx = int(input("Digite Código para excluir: "))

    sql = "DELETE FROM clientes WHERE id_clientes = %d;" % idEx

    c = conn.cursor()
    try:
        c.execute(sql)
        conn.commit()

        if c.rowcount > 0:
            print("\nCódigo: %d, excluido com sucesso" % idEx)
        else:
            print("Nenhum registro foi excluido!")

        input("")
    except:
        raise Exception("Erro, Não foi possivel excluir.")
    finally:
        c.close()
        conn.close()
