import sqlite3

conn = sqlite3.connect('banco_SQLite/bancos/docs_site.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM estoques ORDER BY preco'):
    # Exbie todas as linhas e colunas, tipo uma Tupla
    print(row)
    # print(row[0], row[1])

conn.close()