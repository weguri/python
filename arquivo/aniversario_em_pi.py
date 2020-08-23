file_path = '../arquivo_txt/pi_digitos.txt'
try:
    with open(file_path) as file_obj:
        linhas = file_obj.readlines()

    aniversario = input('Insira sua data de nascimento, no formato mmddyy: ')

    if aniversario in linhas:
        print('Seu aniversário aparece no primeiro milhão de dígitos de pi')
    else:
        print('Seu aniversário não aparece no primeiro milhão de dígitos de pi')

except FileNotFoundError as e:
    print('Arquivo não localizado')
