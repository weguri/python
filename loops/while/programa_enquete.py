respostas = dict()

# Define uma flag para indicar que a enquete está ativa
votacao_ativa = True

while votacao_ativa:
    # Pede o nome da pessoa e a resposta
    nome = input("\nQual é o seu nome? ")
    resposta = input("Qual é o seu animal favorito? ")
    if resposta == "":
        continue

    # Armazena a resposta no dicionario
    respostas[nome] = resposta

    # Perguntar se deseja continuar ou não
    repetir = input("Deseja incluir mais algum animal?(S/N) ")
    if repetir.lower() == 'n':
        votacao_ativa = False

# A enquete foi concluída. Mostra os resultados
print('\n', '-' * 12, 'Resultado', '-' * 12)
for nome, resposta in respostas.items():
    print("%s é o animal favorito do %s" % (resposta, nome))
