from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
A MySQLCursorDict classe nos permite acessar linhas como dicionários, 
em vez de uma tupla.
"""


try:
    conn = ConexaoDB().conexao()

    # Resultado retona no formato dicionario
    cursor = conn.cursor(dictionary=True)

    try:
        # Executar o SQL
        cursor.execute("SELECT nome_clientes, telefone_clientes "
                       "FROM clientes LIMIT 1")

        # rowcount iria exibir -1
        print("número de linhas (inicial):", cursor.rowcount, end="\n\n\n")

        # Acessando as duas colunas do select
        for row in cursor:
            print(row)
            print(row['nome_clientes'], row['telefone_clientes'], sep="  --  ")

        # Exibir numero de linhas existente na tabela
        print("\n\nnúmero de linhas (inicial):", cursor.rowcount)

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
