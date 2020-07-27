import mysql.connector
from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
Todas as classes de exceção para lidar com erros e avisos são 
definidas no mysql.connector.errors módulo

A mysql.connector.errors.Error é a classe base para todas as outras exceções. 
Podemos usá-lo para capturar qualquer tipo de exceção.
"""

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    # A tabela não existe
    sql = """ select * from tabela_nao_existe limit 5 """
    cursor.execute(sql)

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(err)
    print("Error código:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Menssagem", err.msg)
