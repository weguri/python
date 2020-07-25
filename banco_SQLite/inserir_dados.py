import sqlite3

try:
    conn = sqlite3.connect("banco_SQLite/bancos/pessoas.db")
    c = conn.cursor()

    # A tabela foi criada no outro aquivo criar_banco_tabela.py

    # Insert
    sql = "INSERT INTO pessoa VALUES "\
        "(NULL, 'Weliton', 'guri@email.com'), "\
        "(NULL, 'Maria', 'maria@email.com'), "\
        "(NULL, 'Ivo', 'ivo@email.com'), "\
        "(NULL, 'Gabi', 'gabi@email.com'), "\
        "(NULL, 'Nice', 'nice@email.com')"

    try:
        # Deletar Dados(para testar)
        c.execute("DELETE FROM pessoa;")

        c.execute(sql)

        # Confirma a transação
        conn.commit()

    except sqlite3.OperationalError as err:
        # Fechar o leitor do banco
        c.close()

        # Fechar conexão
        conn.close()
        print("Erro:", err)

except sqlite3.OperationalError as err:
    print("Erro:%s" % err)
except sqlite3.IntegrityError as err:
    print("Erro: %s" % err)
else:
    print("Sucesso")
