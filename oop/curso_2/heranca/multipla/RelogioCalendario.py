from oop.curso_2.heranca.multipla.calendario import Calendario
from oop.curso_2.heranca.multipla.relogio import Relogio

"""
Herança Múltipla
"""


class RelogioCalendario(Relogio, Calendario):
    def __init__(self, hora, minuto, segundo, dia, mes, ano):
        """
        Toda variável utilizada na classe Relogio e Calendario
        :param hora:
        :param minuto:
        :param segundo:
        :param dia:
        :param mes:
        :param ano:
        """

        # Colocando desta forma: var = var
        #   não vai gerar ERRO quando mudar a ordem da chamada da classe
        super(RelogioCalendario, self).__init__(hora=hora, minuto=minuto, segundo=segundo, dia=dia, mes=mes, ano=ano)

        """
        Desta forma gera erro caso mude a ordem das classes
                super(RelogioCalendario, self).__init__(hora, minuto, segundo, dia, mes, ano)
        
        Exemplo abaixo funciona normalmente, mais por regra é sempre importante utilizar o comando super
                Relogio.__init__(self, hora, minuto, segundo)
                Calendario.__init__(self, dia, mes, ano)
        """

    def __repr__(self):
        # Gera erro pois nas duas classes tem o metodo __repr__
        # super(RelogioCalendario, self).__repr__()
        #
        return Relogio.__repr__(self) + ' ' + Calendario.__repr__(self)

    def tick(self):
        hora_anterior = self.hora

        # Chamar o metodo da classe Relogio
        # pois o metodo nesta classe tem outro comportamento
        super(RelogioCalendario, self).tick()

        if self.hora < hora_anterior:
            self.avancar()


# Teste
rel_cal = RelogioCalendario(23, 59, 59, 31, 12, 2020)
print(rel_cal)
rel_cal.tick()
print(rel_cal)

#
# mro = mostra a ordem que as classes seram executadas
print(
    "\nOrdem executadas:\n",
    RelogioCalendario.mro()
)
