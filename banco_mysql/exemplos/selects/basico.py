from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    try:
        """ Faz a consulta e um For para exibir as linhas """
        cursor.execute("SELECT * FROM clientes")
        for row in cursor:
            # print(row)  # Exibi toda a linha como um tupla
            print(row[0], row[1])
    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
