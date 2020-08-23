"""
return
    Retorna a informação processada dentro da função
    Este comando faz com que a função pare neste ponto
"""


def cumprimentar_usuario(nome: str, idade: int = 0, olhos: str = "castanho") -> str:
    """Função retorna os dados, comando return"""
    str_idade = ''
    if idade > 0:
        str_idade = '\nTenho ' + str(idade) + ' anos'

    frase = f"Ola! {nome.title()}{str_idade}\nCor dos meus olhos é, {olhos}"
    return frase


retorno_func = cumprimentar_usuario("alejandro", 29, 'azul')
print(retorno_func, end='\n\n')

retorno_func = cumprimentar_usuario("pablo")
print(retorno_func, end='\n\n')
