from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
Por padrão o objeto cursor converte automaticamente os tipos MySQL
em seus tipo equivalentes em Python

Para que não ocorra isso passe no metodo cursor o valor raw=True
"""


try:
    conn = ConexaoDB().conexao()

    # cursor não processado 
    cursor = conn.cursor(raw=True)

    try:
        # Executar o SQL
        cursor.execute("SELECT * FROM clientes LIMIT 3")

        # rowcount iria exibir -1
        print("número de linhas (inicial):", cursor.rowcount, end="\n\n\n")

        # 
        cursor.fetchall()

        # Exibir numero de linhas existente na tabela
        print("\n\nnúmero de linhas (inicial):", cursor.rowcount)
        
    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
