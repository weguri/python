from include.conexao import ConexaoDB


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
            'nome': "Maia",
            'fone': "1111-9999",
            'email': 'text@tex.com',
            'id': 17
        },
        {
            'nome': "Gabi",
            'fone': "2212-3400",
            'email': 'afgha@teste.com',
            'id': 3
        },
        {
            'nome': "Sergio",
            'fone': "3331-2223",
            'email': 'saida@tes.com.br',
            'id': 1
        },
    ]

    # Fazendo a inserção de todos os registros
    # Sem usar um FOR para execultar o SQL
    cursor.executemany(sql, data_list)

    conn.commit()

    print(cursor.rowcount, "registro(s) atualizado.")

except Exception as err:
    print(err)
else:
    cursor.close()
    conn.close()
