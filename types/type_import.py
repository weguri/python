import types


def mostrarTipos(info):
    tipo = type(info)

    if tipo == str:
        return "String"
    elif tipo == int:
        return "Inteiro"
    elif tipo == list:
        return "Lista"
    elif tipo == dict:
        return "Dicionario"
    elif tipo == float:
        return "Numero decimal"
    elif tipo == tuple:
        return "Tupla ()"
    elif tipo == types.BuiltinFunctionType:
        return "Função interna"
    elif tipo == types.FunctionType:
        return "função simples"
    else:
        return "Ultimo Else: {}".format(str(tipo))

tupla = ()

print(mostrarTipos("Segior"))
print(mostrarTipos(33))
print(mostrarTipos(2.2))
print(mostrarTipos({}))
print(mostrarTipos([]))
print(mostrarTipos(tupla))
print(mostrarTipos(print))

print(mostrarTipos(None))
