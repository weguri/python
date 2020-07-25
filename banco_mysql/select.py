import mysql.connector

try:
    conn = mysql.connector.connect(user='root',
                                   password='xs9d2m!13N@1p',
                                   host='127.0.0.1',
                                   database='udemy_neri')
    c = conn.cursor()

    try:
        c.execute("select * from pessoas")
        result = c.fetchall()

        for rs in result:
            print(
                "Código..: %d, Nome..:%s, E-mail..: %s, Idade..: %d" %
                  (rs[0], rs[1], rs[2], rs[3],)
            )
    except mysql.connector.errors.ProgrammingError as err:
        print(err)
    finally:
        c.close()
        conn.close()
except mysql.connector.errors.ProgrammingError as err:
    print(err)
