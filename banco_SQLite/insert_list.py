import sqlite3

try:
    conn = sqlite3.connect("banco_SQLite/bancos/pessoas.db")
    c = conn.cursor()

    # List do que vai ser inserido no banco
    dados = [
        ("Antonio", "ant@email.com"),
        ("Carla", "carla@email.com"),
        ("Gostosa", "gata@email.com"),
    ]

    strSQL = "INSERT INTO pessoa VALUES (NULL, ?, ?)"

    try:
        # prepared statement
        # Desta forma insere TUDO de uma vez
        # c.executemany(strSQL, dados)

        # Inserir varios dados
        for r in dados:
            c.execute(strSQL, r)

        conn.commit()

    except sqlite3.OperationalError as err:
        c.close()
        conn.close
        print("Erro:", err)

    c.close()
    conn.close

except sqlite3.OperationalError as err:
    print("Erro: %s" % err)
else:
    print("Sucesso")