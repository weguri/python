import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(user='root',
                                  password='xs9d2m!13N@1p',
                                  host='127.0.0.1',
                                  database='udemy_neri')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está errado com seu nome de usuário ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe")
    else:
        print(err)
else:
    conn.close()
