from include.conexao import ConexaoDB

""" 
A MySQLCursorNamedTuple classe cria um cursor que retorna linhas como namedtuple.

Para criar uma MySQLCursorNamedTuplepassagem named_tuple=Truepara o cursor() 
método do objeto de conexão.
"""


try:
    conn = ConexaoDB().conexao()

    # classe cria um cursor que retorna linhas como namedtuple.
    cursor = conn.cursor(named_tuple=True)

    try:
        # Executar o SQL
        cursor.execute("SELECT nome_clientes, telefone_clientes FROM clientes order by nome_clientes LIMIT 1")

        # rowcount iria exibir -1
        print("número de linhas (inicial):", cursor.rowcount, end="\n\n\n")

        # Resultado, processado por Tupla nomeada
        for row in cursor:
            print(row)
            print(row.nome_clientes, row.telefone_clientes)

        # Exibir numero de linhas existente na tabela
        print("\n\nnúmero de linhas (inicial):", cursor.rowcount)
        
    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
