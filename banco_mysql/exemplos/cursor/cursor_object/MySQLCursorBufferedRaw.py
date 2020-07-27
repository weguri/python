from include.conexao import ConexaoDB

""" 
A MySQLCursorBufferedRaw classe cria um cursor em buffer bruto.
"""


try:
    conn = ConexaoDB().conexao()

    # cursor será bruto e buffered 
    cursor = conn.cursor(raw=True, buffered=True)

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
