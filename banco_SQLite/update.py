import sqlite3

try:
    conn = sqlite3.connect("banco_SQLite/bancos/pessoas.db")
    c = conn.cursor()

    try:
        c.execute("select * from pessoa")
        recset = c.fetchall()
        for r in recset:
            print(r)

        nome = input("\nDigite nome: ")
        email = input("Digite e-mail: ")
        id = int(input("ID para atualizar: "))

        # Update
        c.execute(
            "UPDATE pessoa SET nome_pessoa=?, email_pessoa=? WHERE codigo_pessoa=?", (nome, email, id,))

        conn.commit()

        # Exbir dados da tabela
        c.execute("select * from pessoa where codigo_pessoa=?", (id,))
        recset = c.fetchall()
        for r in recset:
            print("\n")
            print(r)
            print("\n")

    except sqlite3.OperationalError as err:
        print("1 Erro:", err)

    c.close()
    conn.close
except sqlite3.OperationalError as err:
    print("2 Erro: %s" % err)
else:
    print("Sucesso")
