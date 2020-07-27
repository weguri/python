import datetime
import mysql.connector
from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
A MySQLCursorPrepared classe cria um cursor para 
executar a instrução preparada.

Uma instrução preparada, um recurso que nos permite 
reutilizar uma instrução SQL, sem incorrer no custo de compilá-la várias vezes.
"""


try:
    conn = ConexaoDB().conexao()

    # execultar sql com instruções preparadas
    cursor = conn.cursor(prepared=True)

    # Data atual
    hoje = datetime.datetime.now()

    try:
        # Instrução de SQL
        sql1 = """ insert into clientes(nome_clientes, telefone_clientes, email_clientes, aniversario) 
                VALUES (%s, %s, %s, %s) """

            
        data_list = [
            ('Alexandre', '2342-4423', 'teste@mail.com.br', hoje),
            ('Eduardo', '2333-2222', 'teste@mail.com.br', hoje),
            ('Henrique', '1234-4321', 'teste@mail.com.br', hoje),
            ('Felipe', '6786-9986', 'teste@mail.com.br', hoje)
        ]

        cursor.executemany(sql1, data_list)

        # Exibir numero de linhas existente na tabela
        print("\n\nnúmero de linhas (inicial):", cursor.rowcount)

    except mysql.connector.Error as err:
        frase = "\n{}\nError Code:{}\nSQLSTATE:{}\nMessage:{}\n".format(
            err, err.errno, err.sqlstate, err.msg)

        raise Exception(frase)

except Exception as err:
    print(err)
else:
    cursor.close()
    conn.close()
