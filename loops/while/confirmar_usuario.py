"""
Montar:
    Começa com os usuários que precisam ser verificado
    e com  um lista vazia para os usuários confirmados

    Verifica cada usuário até que não haja mais usuários não confirmados
    Transfere cada usuário verificado para a lista de usuários confirmados
"""

usuarios_nao_confirmados = ['isabel', 'juan', 'vicente']
users_confirmados = []

while usuarios_nao_confirmados:
    users_atual = usuarios_nao_confirmados.pop()
    print("verificando usuário:", users_atual.title())
    users_confirmados.append(users_atual)

#
# Exibe todos os usuários confirmados
print("\nOs seguintes usuários foram confirmados:")
for user in users_confirmados:
    print(user.title())
