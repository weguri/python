import pathlib

file_path = '../arquivo_txt/lista_convidado.txt'

try:
    arq_existe = pathlib.Path(file_path)
    tip = 'w'
    if arq_existe.exists():
        tip = 'a'

    with open(file_path, tip) as file_object:
        primeira_linha = ('-' * 10) + ' Lista de convidados ' + ('-' * 10)

        print(primeira_linha)
        file_object.write(primeira_linha + '\n')
        while True:
            nome = input('Digite \'s\' sair.\nNome do convidado: ')
            if nome.lower() == 's':
                break

            file_object.write(nome + '\n')


except FileNotFoundError as e:
    print('Não foi possivel criar o arquivo')
    print(e)
