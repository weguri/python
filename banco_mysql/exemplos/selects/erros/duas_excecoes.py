from configparser import Error
from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    c.execute("SELECT * FROM clientes")

    # o conjunto de resultados da consulta acima não é lido 
    # agora estamos executando um novo 
    # 
    # Caso tente execultar outro select sem processar o anterior 
    # Gera um erro
    #   Erro: Unread result found

    c.execute("SELECT * FROM pessoas")

    for row in c:
        print(row)

    c.close()
    conn.close()

except Exception as err:
    print("Erro:", err)
