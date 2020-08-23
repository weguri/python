class Carros:
    """Uma tentativa simples de representar um carro"""

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        """Inicializar os atributos que descrevem um carro"""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.leitura_odometro = 0

    def get_nome_descritivo(self) -> str:
        """Devolve um nome descritivo, formatado de modo elegante"""
        nome_longo = str(self.ano) + ' ' + self.marca + ' ' + self.modelo
        return nome_longo.title()

    def ler_odometro(self) -> None:
        """Exibir uma frase que mostra km do carro"""
        print('Km rodado ' + str(self.leitura_odometro))

    def atualizar_odometro(self, kms: int) -> None:
        """
        Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor para hodômetro
        """
        if kms >= self.leitura_odometro:
            self.leitura_odometro = kms
        else:
            print('Você não pode reverter um hodômetro!')

    def incrementar_odometro(self, km: int) -> None:
        """Soma a quantidade especificada ao valor de leitura do odômetro"""
        self.leitura_odometro += km

    def tanque(self) -> None:
        print('Carro movido com Combustível líquido.')


if __name__ == "__main__":
    meu_carro_novo = Carros('Audi', 'A4', 2016)
    print(meu_carro_novo.get_nome_descritivo())
    meu_carro_novo.ler_odometro()

    # Atualizar a km do carro
    meu_carro_novo.atualizar_odometro(12)
    meu_carro_novo.ler_odometro()

    # Atualizar a km do carro
    # Não é possivel inserir um valor menor do que foi o anterior
    meu_carro_novo.atualizar_odometro(9)

    #
    # Atualizar
    meu_carro_novo.atualizar_odometro(200)
    meu_carro_novo.ler_odometro()

    #
    # Incrementar
    meu_carro_novo.incrementar_odometro(1000)
    meu_carro_novo.ler_odometro()
