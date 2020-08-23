"""
Dicionario
    Vazio
        d = {}
        d = dict()

    Com Valor
        d = {'jose': 22, 'roberto': 10}
"""

d = dict()
# print(type(d))  # retorna: <class 'dict'>
d['jose'] = 22
d['roberto'] = 10

print(d)

print(d.get('jose'))
# ou
print(d['jose'])

# print(d.get('mara')) # Retorna None
