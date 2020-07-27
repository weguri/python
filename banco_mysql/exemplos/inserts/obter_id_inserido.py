from include.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """ INSERT INTO clientes (nome_clientes, telefone_clientes, email_clientes) 
                VALUES (%s, %s, %s) """

    val = ("João", "1111-1111", "wetestl@tes.com")

    c.execute(sql, val)
    conn.commit()

    # Retorna o ID do ultimo inserte
    print("1 registro inserido, ID:", c.lastrowid)

    # Total de linha inseridas
    print(c.rowcount, "registro inserido.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
