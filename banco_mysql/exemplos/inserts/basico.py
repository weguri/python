from include.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """INSERT INTO clientes (nome_clientes, telefone_clientes, email_clientes) VALUES (%s, %s, %s)"""
    val = ("João", "1111-1111", "wetestl@tes.com")

    c.execute(sql, val)
    conn.commit()

    print(c.rowcount, "registro inserido.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
