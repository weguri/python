import sqlite3

try:
    conn = sqlite3.connect("banco_SQLite/bancos/pessoas.db")
    c = conn.cursor()

    try:
        c.execute("select * from pessoa")
        recset = c.fetchall()
        for r in recset:
            print(r)
        
        # Entrando com ID para exclusão
        apagar = int(input("\nDigite o ID para exclusão: "))

        # Excluir 
        c.execute("DELETE FROM pessoa WHERE codigo_pessoa=?", (apagar,))

        conn.commit()
    except sqlite3.OperationalError as err:
        print("1 Erro:",err)

    c.close()
    conn.close
except sqlite3.OperationalError as err:
    print("2 Erro: %s" % err)
else:
    print("Sucesso")