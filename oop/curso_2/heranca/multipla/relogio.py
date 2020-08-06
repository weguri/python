class Relogio:
    def __init__(self, hora=0, minuto=0, segundo=0, *args, **kwargs):
        super(Relogio, self).__init__(*args, **kwargs)
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def ajustar_hora(self, hora, minuto, segundo=0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def __repr__(self):
        # Desta forma gera um erro na classe RelogioCalendario
        #
        # return "{0:02d}:{1:02d}:{2:02d}".format(self.hora, self.minuto, self.segundo) +
        # ' ' + super(Relogio, self).__repr__()
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hora, self.minuto, self.segundo)

    def tick(self):
        if self.segundo == 59:
            self.segundo = 0
            if self.minuto == 59:
                self.minuto = 0
                if self.hora == 23:
                    self.hora = 0
                else:
                    self.hora += 1
            else:
                self.minuto += 1
        else:
            self.segundo += 1

# Testar a classe
# rel = Relogio(10, 3, 59)
# rel = Relogio()
# print(rel)
#
# rel.tick()
#
# print(rel)
