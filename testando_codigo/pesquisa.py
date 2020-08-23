class PesquisaAnonima:
    """ Coleta resposta anônimas para uma pergunta de uma pesquisa """

    def __init__(self, questao: str) -> None:
        """ Armazena uma pergunta e se prepara para armazenar as pespostas """
        self.questao = questao
        self.respostas = []

    def mostra_questao(self):
        """ Mostra a pergunta da pesquisa """
        print(self.questao)

    def armazenar_resposta(self, novo_resposta):
        """ Armazena uma uníca resposta da pesquisa """
        self.respostas.append(novo_resposta)

    def mostra_resultado(self):
        """ Mostra todas as respostas dadas """
        print('Resultado da pesquisa:')
        for resposta in sorted(self.respostas):
            # num = self.respostas.count(resposta)
            print(f'\t- {resposta}')
