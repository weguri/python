
""" 
    Creacion dinamica de variables
    diccionario de variables globales
"""
g = globals()


def crear_variables(numero, cadena='var',
                    lista_valores=None,
                    inicio=1):

    fin = inicio + numero

    for i, j in enumerate(range(inicio, fin)):
        if lista_valores:
            valor = lista_valores[i]
        else:
            valor = None

        g[cadena+str(j)] = valor



""" 
Lista de exemplo de Uso
"""


crear_variables(4)
# var1 var2 var3 var4

crear_variables(3, 'num', (1, 2, 3, 4))
# num1 num2 num3

crear_variables(5, 'letra', 'd e f g h'.split(), inicio=4)
# letra4 letra5 letra6 letra7 letra8


variables_creadas = 'var1 var2 var3 var4 num1 num2 num3 letra4 letra5 letra6 letra7 letra8'.split()

for variable in variables_creadas:
    print(variable, '=', eval(variable))
