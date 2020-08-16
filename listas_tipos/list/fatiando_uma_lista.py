""" 
Intervalo de índices
    Você pode especificar um intervalo de índices
    especificando por onde começar e por onde terminar o intervalo.

    Ao especificar um intervalo, o valor
    retornado será uma nova lista com os itens especificados.
"""

# Nota: A pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).
lista = ["oxicoco", "maça", "kiwi", "melon", "abacaxi", "banana", "mango", "ananás"]

print("""Apresentar somente as posições pares""")
print(lista[1:8:2])
print(lista[::2])

print("""\nApresentar da 2º posição até a 5º""")
print(lista[2:5])

print("""\nApresentar as 4 primeiras posições""")
print(lista[:4])

print("""\nApresentar da 3º posição até o fim""")
print(lista[3:])

print("""\nApresentar as 2 ultimas posições""")
print(lista[-2:])

print("""\nRetira a primeira e a ultima posição""")
print(lista[1:-1])
