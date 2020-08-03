import random

# Aleatório de 1 até 50
for num in range(4):
    print(random.randint(1, 50))

print('-' * 30)

# Irá gerar valores 0 a 1
for num in range(4):
    aleatorio = random.random()
    print(aleatorio, "|  Round:".rjust(15), round(aleatorio, 3))

print('-' * 30)

# Aleatório de valores ponto flutuante
for num in range(4):
    aleatorio = random.uniform(20, 30)
    print(aleatorio, "|  Round:".rjust(15), round(aleatorio, 3))

# Embaralhada na List
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
random.shuffle(lista)
print(lista)
