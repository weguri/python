"""
Mesmo resultado do que foi feito neste arquivo:
    map_math.py

    substituir uma chamada a map() por list comprehensions.
"""

import math

lista = [2, 5, 6, 9, 12]
lista = [math.sqrt(x) for x in lista]
print(lista)

lista = [math.sqrt(x) for x in range(10)]
print(lista)