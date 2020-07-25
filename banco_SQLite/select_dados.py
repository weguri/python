import sqlite3

try:
    conn = sqlite3.connect("banco_SQLite/bancos/pessoas.db")
    c = conn.cursor()

    # SQL
    sql = "select * from pessoa"

    c.execute(sql)

    # Recuperando o resultado da pesquisa
    recset = c.fetchall()

    # Listando dados do banco
    for r in recset:
        print(r)
        # print(r[0], r[1])
    
    c.close()
    conn.close()

except sqlite3.OperationalError as err:
    print("Erro: %s" % err)
else:
    pass
