"""
var_list = list(lista)
    Criar list que aponte para posição diferente da memoria
        Não sendo a mesmo lista
"""

frutas = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# nova_lista = list(lista)  # Fazer uma copia
# ou
nova_frutas = frutas[:]  # Fazer uma copia

nova_frutas.pop()
nova_frutas.pop(1)  # remover uma posição específica
nova_frutas.pop()

print("Original:", frutas, sep="\n", end="\n\n")

print("Posições removidas:", nova_frutas, sep="\n", end="\n")
