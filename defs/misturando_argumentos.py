"""
Misturando argumentos posicionais e arbitrários
*cobertura
    Ex:
        fazer_pizza(1º, 2º, 3º, 4º)
            - 1º argumento é atribuido para numero_pedacos
            - 2º, 3º, 4º são atribuido para *cobertura
"""


def fazer_pizza(numero_pedacos: int, *cobertura):
    """Apresenta a pizza que estamos prestes a preparar"""

    print('\nFazendo uma pizza de ' + str(numero_pedacos) + ' pedaços com as seguintes coberturas::')
    for recheio in cobertura:
        print('-', recheio)


fazer_pizza(12, 'pepperoni')
fazer_pizza(8, 'cogumelos', 'pimentão verde', 'queijo extra')
