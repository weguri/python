from include.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    # c = conn.cursor(prepared=True)
    c = conn.cursor()

    sql = """ INSERT INTO clientes (id_clientes, nome_clientes, telefone_clientes, email_clientes, aniversario_clientes) 
                    VALUES (%(id)s, %(nome)s, %(fone)s, %(email)s, NOW()) 
                    ON DUPLICATE KEY UPDATE 
                        id_clientes = %(id)s, 
                        nome_clientes = %(nome)s, 
                        telefone_clientes = %(fone)s, 
                        email_clientes = %(email)s;
            """
    # val = {'id': 1, 'nome': 'Rogerio', 'fone': '3333-11111', 'email': 'testesaida@tes.com.br'}
    val = {
        "id": 56,
        "nome": "Zé zé ",
        "fone": "1233-7777",
        "email": "t@tes.com.br"
    }
    

    c.execute(sql, val)
    conn.commit()

    print(c.rowcount, "registro inserido.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
