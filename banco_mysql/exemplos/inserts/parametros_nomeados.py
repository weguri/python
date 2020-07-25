from banco_mysql.exemplos.conexoes.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """ INSERT INTO clientes 
                    (nome_clientes, telefone_clientes, email_clientes) 
                VALUES 
                    (%(nome)s, %(fone)s, %(email)s); """

    val = {
        "nome": "Ivanildo",
        "fone": "3442-4424",
        "email": "teste@tes.com.br"
    }

    c.execute(sql, val)
    conn.commit()

    print(c.rowcount, "registro inserido.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
