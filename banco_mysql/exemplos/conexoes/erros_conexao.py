import mysql.connector
from mysql.connector import errorcode

""" 
Para manipular erros de conexão, use a try instrução e 
capture todos os erros usando a exceção errors.Error
"""

try:
    cnx = mysql.connector.connect(
        user='root_errado',
        password='xs9d2m!13N@1p'
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está errado com seu nome de usuário ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe")
    else:
        print(err)
else:
    cnx.close()
