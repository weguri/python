import mysql.connector
from mysql.connector import errorcode
from include.conexao import ConexaoDB

""" 
Exemplo 1: Manipulando o erro genérico

Lembre-se de que ProgrammingError pode capturar uma variedade de exceções, 
que variam de erro de sintaxe a tabela não encontrada. Se você deseja 
capturar algum erro específico, use o errorcode módulo
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
# ProgrammingError - erro generico
#               Mais pode utilizar o errorcode
except mysql.connector.ProgrammingError as err:
    if errorcode.ER_NO_SUCH_TABLE == err.errno:
        print("Tabela não existe")
    else:
        print("Tabela existe")
        # print(err)
        print(err.errno)
        print(err.sqlstate)
        print(err.msg)
except mysql.connector.Error as err:
    print("Algum outro erro aqui...")
    print(err)