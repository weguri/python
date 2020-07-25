from configparser import Error
from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
Passando valores por Dicionario
    consulta com estilo de parâmetro pyformat
"""

try:
    cn = ConexaoDB()
    conn = cn.conexao()
    c = conn.cursor()

    try:
        sql = """ select * from clientes where 
                    nome_clientes like %(nome)s limit %(limite)s; """

        # Dicionario 
        #   identifica as chaves dentro do comando SQL
        dados = {
            'nome': "%wel%",
            'limite': 1
        }

        c.execute(sql, dados)
        for linha in c:
            print(linha)
        
        # retorna numero de linhas obtidas na consulta
        print("Linhas:",c.rowcount)

    except:
        raise Exception("Problema para selecionar")
    finally:
        c.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
