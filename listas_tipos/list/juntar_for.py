""" 
Outra maneira de juntar duas listas é anexando todos os itens da lista2 na lista1, um por um:
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
