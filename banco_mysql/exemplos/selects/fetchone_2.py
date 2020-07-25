from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
fetchone()
    Retorna a próxima linha do conjunto de resultados como tupla. 
    Se não houver mais linhas para recuperar, None será retornado.
"""

try:
    cn = ConexaoDB()
    conn = cn.conexao()
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM clientes limit 5;")
        print(c.fetchone())  # Retorna uma linha
        print(c.fetchmany(2))  # Numero de linha que dever retornar
        print(c.fetchall())  # busca todas as linhas restantes
        print(c.fetchmany())  # o conjunto de resultados agora está vazio

        """ 
        Na linha 1, chamamos fetchone() para ler a primeira linha do conjunto de resultados. 
        Em seguida, chamamos fetchmany() para ler as próximas 2 linhas e, finalmente, chamamos 
        fetchall() para buscar a linha restante. O conjunto de resultados está vazio agora, 
        portanto, a próxima chamada para fetchmany() retorna uma lista vazia.
        """

    except:
        raise Exception("Problema para selecionar")
    finally:
        c.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
