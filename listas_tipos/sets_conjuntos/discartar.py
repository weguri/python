"""
IMPORTANTE
    Nota: Se o item a remover não existir, NÃO discard() gerará um erro.

Para remover um item de um conjunto, use o remove(), ou o discard() método
"""

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
