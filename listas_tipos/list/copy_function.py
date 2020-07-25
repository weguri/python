""" 
copy()
    Existem maneiras de fazer uma cópia, uma maneira é usar o método List incorporado copy().
"""

lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Faça uma cópia de uma lista com o copy() método:
nova_lista = lista.copy()
print(nova_lista)

nova_lista.pop()
nova_lista.pop()
nova_lista.pop()

print(lista)
print(nova_lista)