from include.conexao import ConexaoDB

""" 
Semelhante a MySQLCursorNamedTuple mas cria um cursor em buffer.

Para criar MySQLCursorBufferedNamedTuple passagem named_tuple=True e 
buffered=Truepara o cursor() método do objeto de conexão.
"""


try:
    conn = ConexaoDB().conexao()

    # tupla nomeada com buffer.
    cursor = conn.cursor(named_tuple=True, buffered=True)

    try:
        # Executar o SQL
        cursor.execute(
            "SELECT nome_clientes, telefone_clientes FROM clientes order by nome_clientes LIMIT 1")

        # rowcount iria exibir -1, SEM o buffer
        print("número de linhas (inicial):", cursor.rowcount, end="\n\n\n")

        # Resultado, processado por Tupla nomeada
        for row in cursor:
            print(row)
            print("Nome: {}, Telefone: {}".format(
                row.nome_clientes, row.telefone_clientes))

        # Exibir numero de linhas existente na tabela
        print("\n\nNúmero de linhas (inicial):", cursor.rowcount)

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
