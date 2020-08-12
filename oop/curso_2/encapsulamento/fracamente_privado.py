class FracamentePrivada:
    """
    Exemplo de classe com itens fracamente privados
        Utilizando um underline ( _ )
        Quando utilizado um _ por convenção da liguagem python se deve
        tratar este metodo ou atribudo como privado
        Mais o interpretador do python enxerga tudo sendo public
    """

    def __init__(self):
        self._atributo_fracamente_privado = 520741

    def _metodo_fracamente_privado(self):
        print("Método fracamente privado")


"""
Exemplo: Testar
Classe com itens fracamente privados
"""
p1 = FracamentePrivada()

#
# método fracamente privado
p1._metodo_fracamente_privado()

#
# Atributo fracamente privado
print(p1._atributo_fracamente_privado)
