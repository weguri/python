""" 
Existem vários métodos para remover itens de uma lista:
    remove
        O remove()método remove o item especificado.
    
    pop
        O pop()método remove o índice especificado 
        (ou o último item se o índice não for especificado)

    del
        A delpalavra-chave remove o índice especificado.
    
    clear
        O clear()método esvazia a lista.

"""

lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

lista.remove("banana")
print(lista)

# Remove e retorna a posição
lista.pop()
lista.pop(1)
print(lista)

del lista[0]
print(lista)

lista.clear()
print(lista)