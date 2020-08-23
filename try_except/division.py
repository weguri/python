print('Dê-me dois números e eu os dividirei')
print('Entre com \'s\' sair:')

while True:
    primeiro_numero = input("\n1º numero: ")
    if primeiro_numero.lower() == 's':
        break

    segundo_numero = input("2º numero: ")
    if segundo_numero.lower() == 's':
        break

    try:
        # Utilizando o try nesta divisão evita que sistema
        # Gere um erro, provocando sistema travamento
        resposta = int(primeiro_numero) / int(segundo_numero)
    except ZeroDivisionError as e:
        print('Você não pode dividir por 0!')
    else:
        print(resposta)
