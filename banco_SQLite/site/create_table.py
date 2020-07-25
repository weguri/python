import sqlite3

"""
Site https://docs.python.org/3/library/sqlite3.html
    Tutorial com explicação
"""

conn = sqlite3.connect('banco_SQLite/bancos/docs_site.db')
c = conn.cursor()

# Criar tabela
c.execute('''CREATE TABLE estoques
             (data text, encontro text, simbolo text, qty real, preco real)''')

# Inserir uma linha de dados
c.execute("INSERT INTO estoques VALUES ('2020-07-11','COMPRAR','RHAT',100,35.14)")

# Salvar (confirmar) as alterações
conn.commit()

# Também podemos fechar a conexão se terminarmos com ela.
# Certifique-se de que quaisquer alterações foram confirmadas ou elas serão perdidas.
conn.close()
