import sqlite3

# Conexão
conn = sqlite3.connect('banco_SQLite/bancos/docs_site.db')

# Curso
c = conn.cursor()

# Nunca faça isso - inseguro!
# symbol = 'RHAT'
# c.execute("SELECT * FROM estoques WHERE simbolo = '%s'" % symbol)

# prepared statement
# JEITO CERTO: Faça isso
t = ('RHAT',)
c.execute('SELECT * FROM estoques WHERE simbolo=?', t)
print(c.fetchone()[0])

conn.close()