from banco_mysql.exemplos.conexoes.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """ UPDATE 
                clientes 
            SET 
                nome_clientes = %s,
                telefone_clientes = %s, 
                email_clientes = %s 
            WHERE 
                id_clientes = %s; """

    val = ("Valley 345", "8890-0098", "emai@teste.com.br", 11)

    c.execute(sql, val)
    conn.commit()

    print(c.rowcount, "registro(s) atualizado.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
