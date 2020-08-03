""" 
Tupla Par,
    Entra com uma tupla e retorna uma tupla
    Verificar os indices, e retorna somente os pares
"""


def tupla_par(tupla):
    lista = []
    for i in range(0, len(tupla)):
        if i % 2 == 0:
            lista.append(tupla[i])

    # tuple - converte para uma tupla
    return tuple(lista)


tupla_par(('oi', 'estou', 'estutando', 'python'))

# Função simplificada
def tupla_par1(tupla):
    return tupla[::2]

