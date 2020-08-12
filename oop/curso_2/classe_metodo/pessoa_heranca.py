from datetime import date


class PessoasHeranca:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def desde_ano_nascimento(cls, nome, ano_nascimento):
        return cls(nome, date.today().year - ano_nascimento)

    @staticmethod
    def idade_do_pais(nome, idade_pai, diferenca_idade):
        return PessoasHeranca(nome, (date.today().year - idade_pai + diferenca_idade))

    def exibir(self):
        print("A idade de %s é: %s" % (self.nome, self.idade))


class SexualidadeHumana(PessoasHeranca):
    sex = "Homem"


"""
Metodo classmethod
"""
homem1 = SexualidadeHumana.desde_ano_nascimento("John", 1955)
# print(isinstance(homem1, SexualidadeHumana)) # retorna true
# print(homem1.nome, homem1.idade)
homem1.exibir()


"""
Metodo staticmethod
"""
homem2 = SexualidadeHumana.idade_do_pais("John", 1955, 30)

# Retorna falso, o metodo não pode ser instanciado
# print(isinstance(homem2, SexualidadeHumana))
# print(homem2.idade)
homem2.exibir()
