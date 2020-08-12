class Robo:
    def __init__(self, nome, ano_construcao, lk=0.5, lp=0.5):
        self.nome = nome
        self.ano_construcao = ano_construcao
        self.__potencial_fisico = lk
        self.__potencial_psiquico = lp

    @property
    def condicao(self):
        s = self.__potencial_fisico + self.__potencial_psiquico
        if s <= -1:
            return "Eu me sinto infeliz!"
        elif s <= 0:
            return "Me sinto mal!"
        elif s <= 0.5:
            return "Poderia ser pior!"
        elif s <= 1:
            return "Parece estar bem!"
        else:
            return "Ótimo!"


if __name__ == "__main__":
    x = Robo("Marvin", 1979, 0.2, 0.4)
    y = Robo("Caliban", 1993, -0.4, 0.3)

    print(x.condicao)
    print(y.condicao)
