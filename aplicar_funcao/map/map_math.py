import math

""" 
Função map(), esta solicitando ao interpretador para que execute a função
    aplicar_funcao/map/map_math.py, 
        utilizando os dados da lista
"""

lista = [2, 5, 6, 9, 12]

lista_list = list(map(math.sqrt, lista))
# print(lista_list) # retorna é uma list

lista_map = map(math.sqrt, lista)
# print(listaMap) # retorna: <map object at 0x7f4ce0ad8850>

# Exibir a lista
for x in lista_map:
    print(x)
