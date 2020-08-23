file_path = '../arquivo_txt/pi_digitos.txt'
try:
    with open(file_path) as file_obj:
        linhas = file_obj.readlines()

    string = ''
    for linha in linhas:
        string += linha.strip()

    print(string[:52] + '...')
    print(len(string))

except FileNotFoundError as e:
    print('Arquivo não localizado')
