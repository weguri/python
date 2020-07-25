from mysql.connector import FieldType
from banco_mysql.exemplos.conexoes.conexao import ConexaoDB

""" 
Podemos obter o tipo real da coluna usando a FieldType classe A FieldType classe
fornece todos os tipos de dados suportados do MySQL. Para converter códigos de 
tipo inteiro em sua representação de cadeia, usamos o get_info() método da FieldType 
classe, da seguinte maneira:
"""

try:
    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")
        cursor.fetchall()  # leia o resultado sem imprimir nada

        print("\n\n")

        for desc in cursor.description:
            print("Coluna '{}' é do tipo......: {}".format(
                    desc[0],
                    FieldType.get_info(desc[1])
                )
            )

    except:
        raise Exception("Problema para selecionar")

except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
