class Simples:
    """
    @classmethod
        Pode existir varios construtores
    """

    def __init__(self, nome) -> None:
        """ Construtor padrão """
        self.nome = nome

    @classmethod
    def construtor_secundario(cls, nome):
        return cls(nome)

    @classmethod
    def construtor_terceiro(cls, nome, idade):
        cls.idade = idade
        return cls(nome)


# Acessar construtor padrão
s1 = Simples("Zozelito")

# Acessando segundo construtor
s2 = Simples.construtor_secundario("Amadeu")

# Terceiro construtor
s3 = Simples.construtor_terceiro("Zé", 44)
print(s3.idade)