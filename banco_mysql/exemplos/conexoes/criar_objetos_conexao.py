from mysql.connector import (connection)

""" 
Também é possível criar objetos de conexão usando a classe connection.MySQLConnection () :
"""

cnx = connection.MySQLConnection(user='root',
                                 password='xs9d2m!13N@1p',
                                 host='127.0.0.1',
                                 database='udemy_neri')
cnx.close()
