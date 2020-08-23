import json

"""
Carrega o nome do usuário se foi armazenado anteriormente
Caso contrário, pede que usuário forneça o nome e armazena essa informação
"""


def obter_nome_usuario_armazenado(filepath: str):
    """Obtém o nome do usuário já armazenado se estiver disponível"""
    try:
        # Caso o arquivo não exista, gera um except
        with open(filepath) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError as e:
        return None
    else:
        return username


def obter_novo_usuario(filepath: str):
    username = input("Qual é o seu nome: ")
    with open(filepath, 'w') as f_obj:
        json.dump(username, f_obj)

    return username


def cumprimentar_usuario(filepath: str):
    """Saúda o usuário pelo nome."""
    username = obter_nome_usuario_armazenado(filepath)
    if username:
        print('Bem vindo de volta, %s!' % username)
    else:
        username = obter_novo_usuario(filepath)
        print('Lembraremos de você quando você voltar, %s!' % username)


if __name__ == '__main__':
    filename = (__file__.split('/')[-1])[0:-3]
    filepath = '../../arquivo_txt/' + filename + '.json'

    cumprimentar_usuario(filepath)
