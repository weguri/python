from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
executar a mesma consulta com um conjunto diferente de parâmetros. 
Uma maneira de conseguir isso é chamar o execute()método em um loop
"""

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    sql = """ UPDATE 
                clientes 
            SET 
                nome_clientes = %(nome)s,
                telefone_clientes = %(fone)s, 
                email_clientes = %(email)s 
            WHERE 
                id_clientes = %(id)s; """

    data_list = [
        {
            'nome': "José Maia",
            'fone': "0000-9999",
            'email': 'text@tex.com',
            'id': 17
        },
        {
            'nome': "Gabrielly",
            'fone': "2272-3400",
            'email': 'afgha@teste.com',
            'id': 3
        },
        {
            'nome': "Ferreira Weliton",
            'fone': "2345-2223",
            'email': 'teste@tes.com.br',
            'id': 1
        },
    ]

    """ 
    Utilizando o FOR para execultar cada conjunto do dicionario
    O melhor seria utilizar
        executemany()
    """
    for data in data_list:
        cursor.execute(sql, data)

    conn.commit()

    print(cursor.rowcount, "registro(s) atualizado.")

except Exception as err:
    print(err)
else:
    cursor.close()
    conn.close()