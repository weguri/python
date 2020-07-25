""" 
Não é a forma correta de fazer uma copia na lista

Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: 
list2 será apenas uma referência a list1, e as alterações feitas na list1 
automaticamente também ser feitos em list2.
"""

lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

lista_copiada = lista

print(lista)
print(lista_copiada)

lista.pop()
lista_copiada.pop()
lista_copiada.pop()
lista_copiada.pop()

print(lista)
print(lista_copiada)