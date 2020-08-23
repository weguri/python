def cumprimentar_usuario(nome: str, idade: int = 0, olhos: str = "castanho") -> dict:
    """Retorna um dicionario, com as informações"""
    pessoa = {'nome': nome, 'olhos': olhos}

    if idade:
        pessoa['idade'] = idade

    return pessoa


retorno_func = cumprimentar_usuario(nome="alejandro", olhos="verde")
print(retorno_func, end='\n\n')

#
retorno_func = cumprimentar_usuario("pablo")
print(retorno_func, end='\n\n')

#
retorno_func = cumprimentar_usuario("joaquin", 33)
print(retorno_func, end='\n\n')
