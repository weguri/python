from testando_codigo.nome_function import obter_nome_formatado

print("Entre 's' a qualquer momento para sair")
while True:
    nome = input('\nPor favor, me dê um primeiro nome: ')
    if nome == 's':
        break

    sobrenome = input('Por favor, me dê seu sobrenome: ')
    if nome == 's':
        break

    ultimo_nome = input('Por favor, me dê seu ultimo nome: ')
    if nome == 's':
        break

    formatar_nome = obter_nome_formatado(nome, sobrenome, ultimo_nome)
    print('\tNome perfeitamente formatado: ', formatar_nome)
