from configparser import Error
from include.conexao import ConexaoDB

try:
    conn = ConexaoDB().conexao()
    c = conn.cursor()

    c.execute("SELECT * FROM clientes")

    """ 
    Se as informações não forem processadas antes do fechamento
    Gera um erro
        Erro: Unread result found
    """

    c.close()
    conn.close()

except Exception as err:
    print("Erro:", err)
