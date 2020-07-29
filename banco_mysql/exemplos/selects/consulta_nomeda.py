import datetime
import mysql.connector
from include.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor(prepared=True)

    sql = ("SELECT nome_clientes, telefone_clientes, email_clientes, aniversario "
           "FROM clientes "
           "WHERE aniversario BETWEEN %s AND %s LIMIT 5;")

    dt_inicio = datetime.date(2019, 7, 1)
    dt_fim = datetime.date(2020, 7, 31)

    cursor.execute(sql, (dt_inicio, dt_fim))

    #
    # Retornando as informações para variaveis
    for (nome, fone, email, niver) in cursor:
        print("{}, {}, {}     {:%d %b %Y}\n".format(
            nome, fone.rjust(20), email.rjust(20), niver)
        )

    cursor.close()
    conn.close()
#
# Except de varios erros
except (mysql.connector.IntegrityError, mysql.connector.DataError) as err:
    print("IntegrityError or DataError")
    print(err)

except mysql.connector.ProgrammingError as err:
    print("ProgrammingError")
    print(err)

except mysql.connector.Error as err:
    print(err)
