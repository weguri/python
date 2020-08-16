"""
Unir as duas lista
    for
        fazendo um loop sobre a lista

    Extend() método
        objetivo é adicionar elementos de uma lista para outra lista.

    +
        usando operado + (mais)

"""

lista_1 = ["oxicoco", "maça", "kiwi", "melon"]
lista_2 = ["abacaxi", "banana", "mango", "ananás"]

#
print("""Exemplo 1 : +""")
lista_3 = lista_1 + lista_2  # ajuntar lista
print(lista_3)

#
print("""\nExemplo 2 : for""")
for x in lista_2:
    lista_1.append(x)
print(lista_1)

#
# OBSERVAÇÂO: a lista nesta parte vai ficar maior por causa do For
print("""\nExemplo 3 : extend""")
lista_1.extend(lista_2)  # Use o extend() método para adicionar a lista2 no final da lista1.
print(lista_1)
