class Magica:
    def __init__(self, nome):
        self.nome = nome

    # É chamado quando um atributo é acessado
    def __getattribute__(self, item):
        print('__getattribute__', item)
        return super(Magica, self).__getattribute__(item)

    # É chamado quando o item não é encontrado via __getattribute__
    def __getattr__(self, item):
        print('__getattr__', item)
        return super(Magica, self).__setattr__(item, 'órfão')


mg = Magica('Abracadabra')
print(mg.nome)

print()

mg.truque = "Show de Cartas"
print(mg.truque)

print()

mg.assistente
print(mg.assistente)
