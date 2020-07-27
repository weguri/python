from configparser import Error
from include.conexao import ConexaoDB

""" 
fetchone()
    Retorna a próxima linha do conjunto de resultados como tupla. 
    Se não houver mais linhas para recuperar, None será retornado.
"""

try:
    cn = ConexaoDB()
    conn = cn.conexao()
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM clientes;")

        # Obter primeira linha
        #   Caso tenha mais linha para ser exibida e não o fizer 
        #   gera erro no metodo
        linha = c.fetchone()

        while linha:
            print(linha)
            linha = c.fetchone()
    except:
        raise Exception("Problema para selecionar")
    finally:
        c.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
