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
        column_names
            Retorna os nomes das colunas como uma 
            tupla a partir da qual os dados são retornados. """

        print("column_names:", cursor.column_names, end='\n\n')

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
