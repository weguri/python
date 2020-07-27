from include.conexao import ConexaoDB

""" 
Neste exemplo utilizando o buffered para obter as informações da tabela 
O rowcount antes e depois do For ira motrar o mesmo valor total de linha na tabela
"""


try:
    conn = ConexaoDB().conexao()

    # criar um cursor em buffer
    cursor = conn.cursor(buffered=True)

    try:
        # Executar o SQL
        cursor.execute("SELECT * FROM clientes")

        # Exibir numero de linhas existente na tabela
        # Sem o buffer o rowcount iria exibir -1
        print("número de linhas (inicial):", cursor.rowcount)

        # O FOR neste exemplo é só para consumir os dados
        # Para visualizar os dados é só utilizar print(row)
        for row in cursor:
            pass

        # Exibir numero de linhas existente na tabela
        print("número de linhas (inicial):", cursor.rowcount)
        
    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
