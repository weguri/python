import datetime
from include.conexao import ConexaoDB

try:
    cn = ConexaoDB()
    conn = cn.conexao()
    c = conn.cursor()

    try:

        sql = ("SELECT nome_clientes, telefone_clientes, email_clientes, aniversario "
               "FROM clientes "
               "WHERE aniversario BETWEEN %s AND %s LIMIT 5;")

        dt_inicio = datetime.date(2019, 7, 1)
        dt_fim = datetime.date(2020, 7, 31)

        c.execute(sql, (dt_inicio, dt_fim))

        # Retornando as informações para variaveis
        for (nome, fone, email, niver) in c:
            print("{}, {}, {}     {:%d %b %Y}\n".format(
                nome, fone.rjust(20), email.rjust(20), niver)
            )

    except:
        raise Exception("Problema para selecionar")
    finally:
        c.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
