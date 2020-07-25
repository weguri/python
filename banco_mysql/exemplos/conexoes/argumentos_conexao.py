import mysql.connector

""" 
raise_on_warnings
    É possível atribuir a essa propriedade um valor de True ou False 
    para ativar ou desativar se os avisos devem gerar exceções. 
"""

config = {
    'user': 'root',
    'password': 'xs9d2m!13N@1p',
    'host': '127.0.0.1',
    'database': 'udemy_neri',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
