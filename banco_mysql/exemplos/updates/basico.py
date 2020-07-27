from include.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """ UPDATE 
                clientes 
            SET 
                nome_clientes = 'Canyon 123',
                telefone_clientes = '2342-0000', 
                email_clientes = 'opac@teste.com' 
            WHERE 
                id_clientes = 8; """

    c.execute(sql)
    conn.commit()

    print(c.rowcount, "registro(s) atualizado.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
