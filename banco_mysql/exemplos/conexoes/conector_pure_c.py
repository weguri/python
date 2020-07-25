import mysql.connector

""" 
Usando a extensão Connector / Python Python ou C
    oferece duas implementações de conexão com:
        Python ou MySQL lib em C

        A configuração use_pure=False faz com que a conexão 
        use a extensão C se a instalação do Connector / Python a incluir, 
        enquanto use_pure=True que False significa que a implementação do 
        Python é usada, se disponível.
"""

# A use_pure opção e a extensão C foram adicionadas no Connector / Python 2.1.1.


cnx = mysql.connector.connect(user='root',
                              password='xs9d2m!13N@1p',
                              host='127.0.0.1',
                              database='udemy_neri',
                              use_pure=True)
cnx.close()
