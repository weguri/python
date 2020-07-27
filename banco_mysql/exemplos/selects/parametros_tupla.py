from include.conexao import ConexaoDB

""" 
O valor tem que ser passado como UM TUPLE
"""

try:
    cn = ConexaoDB()
    conn = cn.conexao()
    c = conn.cursor()

    try:
        sql = """ select * from clientes where 
                    nome_clientes like %s limit %s; """

        # IMPORTANTE TUPLE
        # ID tem que ser passado como um TUPLE
        #   sem os parentes e a virgula o sitema não entende como um TUPLE
        dados = ("%wel%", 1,)

        c.execute(sql, dados)
        for linha in c:
            print(linha)

    except:
        raise Exception("Problema para selecionar")
    finally:
        c.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
