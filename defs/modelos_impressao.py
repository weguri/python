"""
As list 'designs_nao_impressos' e 'modelos_completos',
    são modificadas fora da função, é tipo uma copia
    copiar uma lista:
        designs_nao_impressos = designs_nao_impressos
            - O problema desta maneira, faz referencia a mesma parte da memoria
            - sendo assim quando modifica uma altera a outra

    Evitando que a list seja modificado
        designs_nao_impressos = designs_nao_impressos[:]
            - Atenção, pois se a lista for muito grande
            - vai esta oculpando mais espaço de memoria
"""


def modelos_impressao(designs_nao_impressos: list, modelos_completos: list):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para modelos_completos após a impressão.
    """
    while designs_nao_impressos:
        design_atual = designs_nao_impressos.pop()

        # Simula a criação de uma impressão 3D a partir do design
        print("Impressão modelo:", design_atual)
        modelos_completos.append(design_atual)


def mostrar_modelos_completos(modelos_completos: list):
    """Mostra todos os modelos impressos"""
    print('\nOs seguintes modelos foram impressos:')
    for modelo in modelos_completos:
        print(modelo)


designs_nao_impressos = ['capa iphone', 'robô pingente', 'dodecaedro']
modelos_completos = []

#
# designs_nao_impressos[:]
#   Desta forma a lista não é esvaziada
#
modelos_impressao(designs_nao_impressos[:], modelos_completos)

#
mostrar_modelos_completos(modelos_completos)
