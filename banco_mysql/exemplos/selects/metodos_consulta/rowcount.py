from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")

        print("Antes do FOR:", cursor.rowcount, end='\n\n')
        
        print("\n")

        # lendo linhas, mas não exibindo
        for row in cursor:
            pass

        """ 
        rowcount
            Retorna o número de linhas produzidas ou afetadas pela última consulta. 
            Para cursores sem buffer, rowcount é inicialmente definido como -1 e é incrementado 
            à medida que as linhas são lidas.
        """

        print("\n")

        print("Depois do FOR:", cursor.rowcount, end='\n\n')

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
