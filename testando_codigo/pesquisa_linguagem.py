from testando_codigo.pesquisa import PesquisaAnonima

# Define uma pergunta e cria uma pesquisa
questao = 'Qual idioma você aprendeu primeiro a falar?'
minha_pesquisa = PesquisaAnonima(questao=questao)

# Mostra a pergunta e armazena as respostas à pergunta
minha_pesquisa.mostra_questao()

print("Entre 's' a qualquer momento para sair")
while True:
    resposta = input('Língua: ')
    if resposta == 's':
        break

    minha_pesquisa.armazenar_resposta(resposta)


# Exibe os resultados da pesquisa
print('\nObrigado a todos que participaram da pesquisa')
minha_pesquisa.mostra_resultado()
