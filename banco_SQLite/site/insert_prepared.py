import sqlite3

conn = sqlite3.connect('banco_SQLite/bancos/docs_site.db')
c = conn.cursor()


# INSERT
# Exemplo maior que insere muitos registros por vez
compras = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
           ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
           ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
           ]

# prepared statement
c.executemany('INSERT INTO estoques VALUES (?,?,?,?,?)', compras)

conn.commit()

conn.close()
