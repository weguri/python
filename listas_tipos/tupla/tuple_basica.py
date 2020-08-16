""" 
Tuple fazia:
    tup = ()
    tup = tuple()
    tup = ("txt",)

As 3 formas acimas retorna..: <class 'tuple'>


Uma tupla é uma coleção ordenada e imutável.
No Python, as tuplas são escritas com parênteses.
"""

frutas_tupla = ("oxicoco", "maça", "kiwi", "melon", "abacaxi", "banana", "mango", "ananás")
print(type(frutas_tupla))  # <class 'tuple'>

# Utilizar o Contrutor
#    tuple()
#
# tuple_contrutor = tuple(["oxicoco", "maça", "kiwi", "melon", "abacaxi", "banana", "mango", "ananás"])
# ou
tuple_contrutor = tuple()
print(type(tuple_contrutor))  # <class 'tuple'>

#
# Utilizando virgula
terminar_virgula = ("apple",)
print(type(terminar_virgula))  # <class 'tuple'>

#
# Sem virgula, NÂO é tuple
sem_virgula = ("apple")
print(type(sem_virgula))  # <class 'str'>
