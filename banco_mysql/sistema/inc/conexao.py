import mysql.connector
from mysql.connector import errorcode


def Conexao():
    BANCO = 'udemy_neri'
    USER = 'root'
    PASSWO = 'xs9d2m!13N@1p'
    HOST = '127.0.0.1'

    try:
        conn = mysql.connector.connect(user=USER,
                                   password=PASSWO,
                                   host=HOST,
                                   database=BANCO)
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise Exception("Algo está errado com seu nome de usuário ou senha")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise Exception("O banco de dados não existe")
        else:
            raise Exception(err)
    finally:
        pass
