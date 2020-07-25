import sqlite3

"""
connect
    criar ou se conectar ao Banco

cursor()
    Com cursor podemos manipular o banco través de SQL
        Create, Insert, Selete
"""
try:
    conn = sqlite3.connect("banco_SQLite/bancos/pessoas.db")

    c = conn.cursor()

    # Instrução de SQL para criar TABELA
    sql = "CREATE TABLE IF NOT EXISTS pessoa "\
        "(codigo_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,"\
        "nome_pessoa VARCHAR(40),"\
        "email_pessoa TEXT)"

    c.execute(sql)

    # Fechar o leitor do banco
    c.close()

    # Fechar conexão
    conn.close()

except sqlite3.OperationalError as err:
    print("Erro:", err)
else:
    print("Tabela criada com sucesso!")