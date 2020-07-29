import mysql.connector
from include.conexao import ConexaoDB

""" 
executemany
    No exemplo do insert ele convete o dicionario em um insert unico
    Em vez de fazer quatro insert faz um unico sendo muito mais eficiente
"""

try:
    db = ConexaoDB().conexao()

    # return a buffered MySQLCursorNamedTuple
    cursor = db.cursor(prepared=True)

    sql1 = """
    create temporary table tmp_clientes(
        id_tmp_clientes int AUTO_INCREMENT PRIMARY KEY,
        nome_tmp_clientes VARCHAR(100) NOT NULL,
        idade_tmp_clientes SMALLINT NOT NULL     
    )
    """

    # 
    # Criar tabela temporaria
    cursor.execute(sql1)

    # 
    # SQL para insert
    sql2 = """
    insert into tmp_clientes(nome_tmp_clientes, idade_tmp_clientes)
    VALUES (%s, %s)
    """

    data_list = [
        ('John', 45),
        ('Max', 25),
        ('Jane', 20),
        ('Bob', 34),
    ]

    
    cursor.executemany(sql2, data_list)

    db.commit()

    # 
    # Numero de linhas inseridas
    print("rowcount:", cursor.rowcount)
    print(cursor)

    #
    # Lista o resultado a saida
    cursor.execute("select * from tmp_clientes")
    for r in cursor:
        print(r)


#
# Except de varios erros
except (mysql.connector.IntegrityError, mysql.connector.DataError) as err:
    print("IntegrityError or DataError")
    print(err)

except mysql.connector.ProgrammingError as err:
    print("ProgrammingError")
    print(err.errno)
    print(err.sqlstate)
    print(err.msg)

except mysql.connector.Error as err:
    print("Error")
    print(err)

else:
    cursor.close()
    db.close()
