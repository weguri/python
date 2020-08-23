def obter_nome_formatado(nome: str, meio: str, ultimo: str = ''):
    """Gera um nome completo formatado de modo elegante"""

    ultimo = ' ' + ultimo if ultimo != '' else ''

    nome_completo = nome + ' ' + meio + ultimo
    return nome_completo
