from include.conexao import ConexaoDB

""" 
Executando várias consultas com execute()

O execute() método aceita um argumento opcional de palavra-chave chamado multi. 
Por padrão, está definido como False. Se definido como True, permite execute()
executar várias consultas separadas por ponto e vírgula. 
Quando chamado com multi=True, o execute() método retorna um iterador que pode 
ser usado para acessar o conjunto de resultados produzido pelas consultas.
"""

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    try:
        sql1 = "SELECT * FROM pessoas LIMIT %s"
        sql2 = "SELECT nome_clientes, email_clientes FROM clientes where nome_clientes=%s"
        sql3 = "SELECT * FROM login"
        sql4 = "select version()"

        queries = [sql1, sql2, sql3, sql4]

        # A desvantagem dessa abordagem é que todos os parâmetros de 
        # consulta devem ser passados ​​em uma única sequência ou mapeamento.
        # 
        # Cada posição da tupla referece uma posição dento do select
        #   Exemplo
        #       3    - primeiro SQL
        #       jonh - segundo SQL
        data = (3, 'John')

        # retorna um iterador
        # object MySQLCursor._execute_iter
        results = cursor.execute(";".join(queries), data, multi=True)
        
        count = 1
        
        for result in results:

            # result é um objeto cursor, ou seja, result == cursor
            # para ter acesso a todos os atributos e métodos do cursor

            print("Query {0} - {1} :".format(count, result.statement))

            # a consulta tem resultado?
            if result.with_rows:
                for row in result:
                    print(row)
                    # print(row[2])
                count = count + 1
            else:
                print("Nenhum resultado encontrado")

            print()

    except:
        raise Exception("Problema para selecionar")
    finally:
        cursor.close()
        conn.close()
except Exception as err:
    print("Erro:", err)
