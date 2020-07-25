""" 
Outra forma de fazer uma copia de lista
Da forma que seja unica
"""

lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

nova_lista = list(lista)
print(nova_lista)

nova_lista.pop()
nova_lista.pop()
nova_lista.pop()

print(lista)
print(nova_lista)