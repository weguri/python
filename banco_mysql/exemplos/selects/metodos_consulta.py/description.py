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
        description
            Retorna uma lista de tuplas contendo informações sobre as 
            colunas no conjunto de resultados. A tupla do formulário 
            (name, type_code, display_size, internal_ size, precision, scale, null_ok). 
            A namerefere-se ao nome da coluna, type_code é um inteiro que indica o tipo
            de coluna e null_okdetermina se uma coluna pode aceitar NULL valores ou não 
            (1 verdadeiros meios e 0 corresponde falsos). O restante dos campos é sempre 
            definido como None.
        """

        print("\n\n")

        print("description: ", end="")
        print(cursor.description)

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
