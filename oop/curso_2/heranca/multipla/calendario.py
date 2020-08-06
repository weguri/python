class Calendario:
    # Atributo
    meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, dia, mes, ano, *args, **kwargs):
        super(Calendario, self).__init__(*args, **kwargs)
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def ajustar_data(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __repr__(self):
        # Desta forma gera um erro na classe RelogioCalendario
        #
        # return "{0:02d}/{1:02d}/{2:4d}".format(self.dia, self.mes, self.ano) +
        # ' ' + super(Calendario, self).__repr__()
        return "{0:02d}/{1:02d}/{2:4d}".format(self.dia, self.mes, self.ano)

    def avancar(self):
        # dia_max = Calendario.meses[self.mes - 1]
        dia_max = self.meses[self.mes - 1]

        if self.dia == dia_max:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1

# Testar classe
# cal = Calendario(31, 1, 2020)
# print(cal)
#
# cal.avancar()
#
# print(cal)
