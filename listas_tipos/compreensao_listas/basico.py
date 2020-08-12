# Apenas números
lista = []

for item in range(10, 20, 2):
    lista.append(item**2)

print(lista)

#
# Podemos reescrevê-lo, utilizando list comprehensions, da seguinte forma:
#
lista = [item**2 for item in range(10, 20, 2)]
print(lista)
