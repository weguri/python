from include.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")

        # lendo linhas, mas não exibindo
        for row in cursor:
            pass

        """ 
        statement
            Retorna a última consulta executada como uma sequência.
        """

        print("\n\n")

        print("statement:", cursor.statement, end='\n\n')

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
