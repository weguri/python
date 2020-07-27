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
        lastrowid	
            Retorna o ID da última linha modificada ou inserida, ou None quando esse 
            valor não estiver disponível (por exemplo, para instruções SELECT). 
            Se várias linhas forem inseridas ou atualizadas, 
            ele retornará apenas o ID da primeira linha.
        """

        print("\n\n")

        print("lastrowid:", cursor.lastrowid, end='\n\n')

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
