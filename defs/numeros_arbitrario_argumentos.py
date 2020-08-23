"""
Asterisco *:
    informa que vai ser passado varios argumentos
"""


def fazer_pizza(*cobertura):
    """Apresenta a pizza que estamos prestes a preparar"""

    print('\nFazendo uma pizza com os seguintes recheios:')
    for recheio in cobertura:
        print('-', recheio)


fazer_pizza('pepperoni')
fazer_pizza('cogumelos', 'pimentão verde', 'queijo extra')
