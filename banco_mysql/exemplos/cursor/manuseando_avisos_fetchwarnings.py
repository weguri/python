from mysql.connector import errors
from include.conexao import ConexaoDB

""" 
Por padrão, o MySQL.Connector/Python não gera uma exceção nos avisos.
Pode alterar isso, passando argumentos no connect()
    get_warnings
        True: avisos, são buscados automaticamente após cada consulta
        Padrão: False
    raise_on_warnings
        True: uma exceção é gerada nos avisos.
        Padrão: False

O fetchwarnings() método retorna uma lista de tuplas contendo o nível 
da mensagem, o código de erro e a própria mensagem gerada pela consulta 
executada anteriormente.
"""

conn = ConexaoDB().conexao()
cursor = conn.cursor()

cursor.execute("CREATE database if not exists udemy_neri;")
print(cursor.fetchwarnings())
# Console:
#   [(bytearray(b'Note'), bytearray(b'1007'), bytearray(b"Can\'t create database \'udemy_neri\'; database exists"))]


cursor.execute("select 1/0;")
cursor.fetchall()  # buscar todas as linhas do conjunto de resultados

print(cursor.fetchwarnings())
# Console:
#   [(bytearray(b'Warning'), bytearray(b'1365'), bytearray(b'Division by 0'))]


cursor.close()
conn.close()
