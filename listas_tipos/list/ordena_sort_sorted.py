"""
sort
    Ordena alfabética

sort(reverse=True)
    Ordem alfabética inversa

sorted
    Ordena temporário, diferente do sort
    pois quando for utilizar a variavel novamente ela vai esta
    na ordem que foi criada
"""

lista = ["oxicoco", "maça", "kiwi", "melon", "abacaxi", "banana", "mango", "ananás"]

print(""" SORT - Ordena """)
lista.sort()
print(lista)

print("""\n lista INVERSA """)
lista.sort(reverse=True)  # inversa
print(lista)


print("""\n SORTED - Ordena temporário """)
print(sorted(lista))  # Ordena temporário
print(sorted(lista, reverse=True))  # Ordena temporário, inverso
print(sorted(lista, reverse=False))  # Ordena temporário, ordem Alfabética
print(lista)  # Exibi originalmente
