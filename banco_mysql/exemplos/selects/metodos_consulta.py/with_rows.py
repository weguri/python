from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")

        # lendo linhas, mas não exibindo
        for row in cursor:
            pass

        """ 
        with_rows
            Um atributo booleano que retorna Truese a consulta 
            produz o conjunto de resultados, caso contrário, ele retorna False.
        """

        print("with_rows:", cursor.with_rows, end='\n\n')

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
