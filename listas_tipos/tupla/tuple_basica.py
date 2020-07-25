""" 
Uma tupla é uma coleção ordenada e imutável . No Python, as tuplas são escritas com colchetes.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# CRIAR TUPLE
# Utilizando o contrutor tuple()
# criar ("text",)

# Contrutor
contrutor_tuple = tuple("apple")
print(type(contrutor_tuple))  # <class 'tuple'>

# Utilizando virgula
terminar_virgula = ("apple",)
print(type(terminar_virgula))  # <class 'tuple'>

# Sem virgula, NÂO é tuple
sem_virgula = ("apple")
print(type(sem_virgula))  # <class 'str'>
