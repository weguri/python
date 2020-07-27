from mysql.connector import errors
from pprint import pprint

""" 
Todas as classes de exceção são mapeadas para uma ou mais 
classes SQLSTATE. Você pode imprimir esse mapeamento digitando o seguinte comando.


A mysql.connector.errors.Error classe base é subclassificada nas 
três classes a seguir:
    DatabaseError
        exceções gerada para erros relacionados ao banco de dados
        Tipo..: Erros na sintaxe SQL, processamento de dados, 
                problemas internos do MySQL

    InterfaceError
        Essa exceção é gerada por erros relacionados à interface 
        (no nosso caso, a interface é MySQL Connector / Python) e 
        não ao próprio banco de dados.

    PoolError
        É gerado para erros relacionados ao pool de conexão.
"""

pprint(errors._SQLSTATE_CLASS_EXCEPTION)