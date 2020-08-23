def passando_lista(lista_nomes):
    """For sobre a lista passada como parametro"""

    for nome in lista_nomes:
        msg = 'Olá, ' + nome + '!'
        print(msg)


users = ['aurora', 'eduarda', 'rebeca', 'manuelly']
passando_lista(users)
