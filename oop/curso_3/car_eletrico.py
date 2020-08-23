from oop.curso_3.bateria import Bateria
from oop.curso_3.car import Carros


class CarroEletrico(Carros):
    """
    CarroEletrico herda atributo e metodos da classe Carros
    Representar aspectos específicos de veículos elétricos
    """

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        """
        Inicializa os atributos da classe pai
        Representar aspectos específicos de veículos elétricos
        Criar uma instâcia
        """
        super().__init__(marca, modelo, ano)
        # self.tamanho_bateria = 70
        self.bateria = Bateria()

    # Este metodo agora esta dentro da classe Bateria()
    # def descritivo_bateria(self) -> None:
    #     """Exibe uma frase que descreve a capacidade da bateria"""
    #     print('Este carro tem bateria de ' + str(self.tamanho_bateria) + '-KWh.')

    def tanque(self) -> None:
        """
        Sobrescrevendo o método da classe-pai
        Carros elétricos não têm tanques de gasolina
        """
        print("Carro elétrico não tem tanque de gasolina")


if __name__ == "__main__":
    meu_tesla = CarroEletrico('tesla', 'Model S', 2018)
    print(meu_tesla.get_nome_descritivo())

    # Acessando o metodo da classe Bateria
    #   Foi feito uma instancia dentro da classe CarroEletrico
    meu_tesla.bateria.descritivo_bateria()
    meu_tesla.bateria.get_alcance()
