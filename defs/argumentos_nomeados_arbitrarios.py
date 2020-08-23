"""
Usando argumentos nomeados arbitrários

**user_info
    Os dois asteriscos fazem o Python cria um dicionario vazio
    colocar quaisquer pares nome-valor recebidos nesse dicionario.



construir_perfil
    Nesse função, podemos acessar os pares nome-valor em user_info como fariamos com qualquer dicionariol
"""


def construir_perfil(nome: str, sobrenome: str, **user_info) -> dict:
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário"""

    perfil = dict(nome=nome, sobrenome=sobrenome)
    for key, value in user_info.items():
        perfil[key] = value

    return perfil


# Variaveis
#   - localidade
#   - campo
#   - idade
#       São passadas para **user_info, e convertida em diciionario
perfil_usuario = construir_perfil('albert', 'einstein', localidade='princeton', campo='physics', idade=76)

print(perfil_usuario)
