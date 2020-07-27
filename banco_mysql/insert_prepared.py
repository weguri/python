import mysql.connector

dados = [
    ("Ivo", "ivo@teste.com", 65),
    ("Sebastião", "sebas@teste.com", 98),
    ("Claudia", "claudia@teste.com", 35),
    ("Charles", "char@teste.com", 33),
    ("nice", "nice@teste.com", 22),
]

strSQL = "INSERT INTO pessoas (nome, email, idade) VALUES (%s, %s, %s);"

try:
    conn = mysql.connector.connect(user='root',
                                   password='xs9d2m!13N@1p',
                                   host='127.0.0.1',
                                   database='udemy_neri')
    c = conn.cursor(prepared=True)

    try:
        # prepared statement
        c.executemany(strSQL, dados)
        conn.commit()

        # Retornar numero de linhas inseridas
        print(c.rowcount, "- Registro inserido com sucesso na tabela Pessoas")

    except mysql.connector.Error as err:
        print("Falha ao inserir registro na tabela MySQL..: {}".format(err))
    finally:
        c.close()
        conn.close()
except mysql.connector.Error as err:
    print("2 -", err)
