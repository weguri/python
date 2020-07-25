from banco_mysql.exemplos.conexoes.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    # Criar Tabela Temporária
    tabelaSQL = """
            create temporary table tmp_cliente(
                id_tmp_cliente int AUTO_INCREMENT PRIMARY KEY,
                nome_tmp_cliente VARCHAR(100) NOT NULL,
                idade_tmp_cliente SMALLINT NOT NULL     
            )
        """

    cursor.execute(tabelaSQL)

    sql2 = """ insert into tmp_cliente(nome_tmp_cliente, idade_tmp_cliente) VALUES (%(nome)s, %(idade)s) """

    data_list = [
        {
            'nome': 'João',
            'idade': 45
        },
        {
            'nome': 'Pedro',
            'idade': 25
        },
        {
            'nome': 'Maria',
            'idade': 20
        },
        {
            'nome': 'Antonio',
            'idade': 34
        },
    ]

    cursor.executemany(sql2, data_list)

    print("Query:", cursor.statement)
    print("Rowcount:", cursor.rowcount)  # rows inserted

    conn.commit()

except Exception as err:
    print(err)
else:
    cursor.close()
    conn.close()
