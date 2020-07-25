import mysql.connector
from mysql.connector import errorcode


class ConexaoDB:
    def __init__(self, banco="udemy_neri", userdb="root", passDB="xs9d2m!13N@1p", hostDB="127.0.0.1"):
        self.banco = banco
        self.userdb = userdb
        self.passDB = passDB
        self.hostDB = hostDB

    def conexao(self):

        try:
            conn = mysql.connector.connect(user=self.userdb,
                                           password=self.passDB,
                                           host=self.hostDB,
                                           database=self.banco,
                                           use_pure=True)
            return conn

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception(
                    "Algo está errado com seu nome de usuário ou senha")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("O banco de dados não existe")
            else:
                raise Exception(err)
        finally:
            pass
