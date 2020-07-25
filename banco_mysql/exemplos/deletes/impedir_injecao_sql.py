from banco_mysql.exemplos.conexoes.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """ DELETE FROM clientes WHERE id_clientes = %s; """
    val = (18,)

    c.execute(sql, val)
    conn.commit()

    print(c.rowcount, "registro(s) deletado.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
