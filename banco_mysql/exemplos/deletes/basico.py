from include.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """DELETE FROM clientes WHERE id_clientes = 18;"""

    c.execute(sql)
    conn.commit()

    print(c.rowcount, "registro(s) deletado.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
