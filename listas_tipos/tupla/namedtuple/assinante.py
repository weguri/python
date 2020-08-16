from collections import namedtuple

Assinante = namedtuple('Assinante', ['email', 'data'])

ass = Assinante('teste@teste.com.br', '2020-08-14')

print(ass)
print(ass.email)
print(ass.data)
