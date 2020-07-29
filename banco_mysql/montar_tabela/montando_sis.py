from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

TABLES = {}
TABLES["clientes"] = (
    "CREATE TABLE IF NOT EXISTS `clientes` ("
    " `id_clientes` int(11) NOT NULL AUTO_INCREMENT,"
    " `nome_clientes` varchar(100) NOT NULL,"
    " `telefone_clientes` varchar(20) NOT NULL,"
    " `email_clientes` varchar(60) NOT NULL,"
    " PRIMARY KEY (`id_clientes`)"
    ") ENGINE=InnoDB;"
)

TABLES["login"] = (
    "CREATE TABLE IF NOT EXISTS `login` ("
    " `id_login` int(11) NOT NULL AUTO_INCREMENT,"
    " `user_login` varchar(100) NOT NULL,"
    " `password_login` varchar(20) NOT NULL,"
    " PRIMARY KEY (`id_login`)"
    ") ENGINE=InnoDB;"
)

TABLES['empregados'] = (
    "CREATE TABLE IF NOT EXISTS `empregados` ("
    "  `id_empregados` int(11) NOT NULL AUTO_INCREMENT,"
    "  `data_nascimento_empregados` date NOT NULL,"
    "  `primeiro_nome_empregados` varchar(14) NOT NULL,"
    "  `ultimo_nome_empregados` varchar(16) NOT NULL,"
    "  `genero_empregados` enum('M','F') NOT NULL,"
    "  `data_contratacao_empregados` date NOT NULL,"
    "  PRIMARY KEY (`id_empregados`)"
    ") ENGINE=InnoDB")

# Criar as tabelas no banco udemy_neri

try:
    conn = mysql.connector.connect(user='root',
                                   password='xs9d2m!13N@1p',
                                   host='127.0.0.1',
                                   database='udemy_neri')
    c = conn.cursor()

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Tabela criada: {} ".format(table_name), end="\n")
            c.execute(table_description)
        except mysql.connector.Error as err:
            print(err.msg)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está errado com seu nome de usuário ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe")
    else:
        print(err)
else:
    c.close()
    conn.close()
