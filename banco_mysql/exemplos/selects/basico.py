from configparser import Error
from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    try:
        """ Faz a consulta e um For para exibir as linhas """
        c.execute("SELECT * FROM clientes")
        for row in c:
            # print(row)  # Exibi toda a linha como um tupla
            print(row[0], row[1])
    except:
        raise Exception("Problema para selecionar")
    finally:
        c.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
