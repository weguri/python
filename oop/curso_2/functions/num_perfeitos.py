""" 
Numero perfeito
Um numero perfeito é um numero inteiro para o qual a soma de todos os
seus divisores positivos, é igual a ele.
"""


def numero_perfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i

    if num == soma:
        return True
    else:
        return False


print(numero_perfeito(6))
