""" 
Depois que um conjunto é criado, 
você não pode alterar seus itens, mas pode adicionar novos itens.

update()
    Para adicionar mais de um item a um conjunto, use o update() método
"""

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)