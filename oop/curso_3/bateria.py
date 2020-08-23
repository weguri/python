class Bateria:
    """Uma tentativa simples de modelar uma bateria para um carro elétrico"""

    def __init__(self, tamanho_bateria: int = 75):
        """Inicializa os atributos da bateria"""
        self.tamanho_bateria = tamanho_bateria

    def descritivo_bateria(self) -> None:
        """Exibe uma frase que descreve a capacidade da bateria"""
        print('Este carro tem bateria de ' + str(self.tamanho_bateria) + '-KWh.')

    def get_alcance(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria"""

        alcance = 240

        if self.tamanho_bateria == 85:
            alcance = 270

        msg = 'Este carro pode percorrer aproximadamente {0} km com carga total'.format(alcance)
        print(msg)
