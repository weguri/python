import mysql.connector
from mysql.connector import errorcode


class ConexaoDB:
    def __init__(self, buffer=False, bruto=False, banco="udemy_neri", userDB="root", passDB="xs9d2m!13N@1p",
                 hostDB="127.0.0.1"):
        """
        Construtor
        :param buffer: False
        :param bruto: False
        :param banco: udemy_neri
        :param userDB: root
        :param passDB: xs9d2m!13N@1p
        :param hostDB: 127.0.0.1
        """
        self.banco = banco
        self.userDB = userDB
        self.passDB = passDB
        self.hostDB = hostDB

        # Indica se é necessário usar a interface pura do Python para o MySQL
        # ou a extensão C que usa a biblioteca cliente do MySQL C:
        # Padrão: False
        self.use_puro = True

        # avisos devem gerar exceções
        # Padrão: False
        self.avisos = True

        # Ative o buffer para todos os objetos de cursor
        # Criados a partir de  esta conexão
        # Padrão: False
        self.buffer = buffer

        # todos os objetos de cursor criados a partir desta conexão serão brutos
        # Caso o valor passado seja True então não se pode utilizar:
        #   conn.cursor(prepared=True) - Pois gera erro
        #
        #   raw = True
        #   .decode() - Nessesario quando o raw é verdadeiro na saida do result
        #
        # Padrão: False
        self.bruto = bruto

    def conexao(self):
        try:
            conn = mysql.connector.connect(user=self.userDB,
                                           password=self.passDB,
                                           host=self.hostDB,
                                           database=self.banco,
                                           use_pure=True,
                                           raise_on_warnings=self.avisos,
                                           raw=self.bruto,
                                           buffered=self.buffer,
                                           charset='utf8'
                                           )
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
