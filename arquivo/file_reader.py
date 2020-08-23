"""
with
    O comando fecha o arquivo depois que não for  mais necessário acessá-lo.

open
    Cria automaticamente o arquivo
    Abre o arquivo para leitura ou escrita

read
    Ler tudo dentro do arquivo
    O comando insere um linha em branco no final

rstrip
    Remove qualquer caracter em branco do lado direito de uma string

readlines
    Armazena cada linha do arquivo em uma lista

For
    fazendo laço de repetição, para ter uma interação em cada linha do arquivo txt
"""

file_path = '../arquivo_txt/pi_32digitos.txt'

try:
    # lISTA TODA INFORMAÇÃO
    print('-' * 10, 'Pega todo conteudo', '-' * 10)
    with open(file_path) as file_object:
        conteudo = file_object.read()
        print(conteudo.rstrip())

    # LINHA A LINHA
    print('\n', '-' * 10, 'Interagindo linha a linha', '-' * 10)
    with open(file_path) as file_object:
        for linha in file_object:
            print(linha.rstrip())

    # LENDO: READLINES
    print('\n', '-' * 10, 'Lendo: readlines()', '-' * 10)
    with open(file_path) as file_object:
        linhas = file_object.readlines()

    for linha in linhas:
        print(linha.rstrip())

    # MANIPULANDO A INFORMAÇÃO
    print('\n', '-' * 10, 'Trabalhando com o conteúdo de um arquivo', '-' * 10)
    with open(file_path) as file_object:
        linhas = file_object.readlines()

    pi_string = ''
    for linha in linhas:
        pi_string += linha.rstrip()  # concatena cada linha

    print(pi_string)
    print(len(pi_string))  # conta  numeor de caracteres


except FileNotFoundError as e:
    print('Arquivo não existe')
