import mysql.connector
from include.conexao import ConexaoDB

""" 
Manipulando vários erros da mesma maneira
"""

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    # A tabela não existe
    sql = """ select * from tabela_nao_existe limit 5 """
    cursor.execute(sql)

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
