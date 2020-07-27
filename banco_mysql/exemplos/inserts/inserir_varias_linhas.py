from include.conexao import ConexaoDB


try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    sql = """ INSERT INTO clientes (nome_clientes, telefone_clientes, email_clientes) 
                VALUES (%s, %s, %s); """

    val = [
        ('Peter', '3453-3453', 'fgdfg@ssdf.com'),
        ('Amy', '2342-4423', 'exemp@xnxx.com'),
        ('Hannah', '5567-7558', 'exemp@xnxx.com'),
        ('Michael', '1123-4421', 'exemp@xnxx.com'),
        ('Sandy', '2123-4421', 'exemp@xnxx.com'),
        ('Betty', '9909-0000', 'exemp@xnxx.com'),
        ('Richard', '8890-4543', 'exemp@xnxx.com'),
        ('Susan', '5839-0339', 'exemp@xnxx.com'),
        ('Vicky', '2342-4442', 'exemp@xnxx.com'),
        ('Ben', '2344-2234', 'exemp@xnxx.com'),
        ('William', '4234-5555', 'exemp@xnxx.com'),
        ('Chuck', '9999-5555', 'exemp@xnxx.com'),
        ('Viola', '5235-3633', 'twes@ccc.com')
    ]

    c.executemany(sql, val)
    conn.commit()

    print(c.rowcount, "registro inserido.")

    c.close()
    conn.close()

except Exception as err:
    print(err)
