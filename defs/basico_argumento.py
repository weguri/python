"""
nome: str
    parametro de entrada, a definição str
    indica que o valor deve ser uma string, mais não é obrigatoriedade

Argumento:
    Pode ser passado um ou varios argumentos

Padrão:
    definir um valor padrão para o parametro
    Observação:
         parametro que tenha valor padrão tem que ser os ultimos
         senão for o ultimo gera erro
    Ex:
        cumprimentar_usuario(nome, idade=100)
"""


def cumprimentar_usuario(nome: str, idade: int, olhos: str = "castanho") -> None:
    """Exibe uma saudação simples com nome da pessao"""
    print('Olá!', nome.title())
    print('Tenho %s anos:' % idade)
    print('Cor dos meus olhos é, %s' % olhos, end='\n\n')


cumprimentar_usuario("alejandro", 29, 'azul')

#
# Posibilidade de utilizar, parametro=valor
#   fora do que foi definido dentro da função
cumprimentar_usuario(idade=43, nome="martina")  # Argumentos nomeados
