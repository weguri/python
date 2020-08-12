""" 
@classmethod
    Poderia se entender como sendo o segundo construtor da classe

@staticmethod
    Seria uma função dentro da classe
    Não pode ser herdado
    Não pode instanciado
"""

class DataMethodStatic:
    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def data_string(cls, dt_string: str):
        dia, mes, ano = DataMethodStatic.dt_str_split(dt_string)

        """
            data:
                nova instancia da classe
            cls:
                Referencia da classe
        """
        data = cls(dia, mes, ano)
        return data

    @staticmethod
    def data_valida(dt_string):
        """ 
        Metodo static
            É uma função dentro da classe
        """
        dia, mes, ano = DataMethodStatic.dt_str_split(dt_string) # chamada para metodo static
        return dia <= 31 and mes <= 12 and ano <= 2030
    
    @staticmethod
    def dt_str_split(dt_string):
        """ 
            Data: 11-08-2020
                split:
                    divide em 3 partes
                int:
                    converte de string para inteiro
                map:
                    faz com que cada valor seja convertido para inteiro
        """
        return map(int, dt_string.split('-'))

    # Quando for imprimir a instancia da classe
    # Este metodo é chamado automaticamente
    def __repr__(self) -> str:
        return f"{str(self.dia).zfill(2)}/{str(self.mes).zfill(2)}/{self.ano}"


""" Exemplo de Uso """

# Chamando o construtor da classe
data_1 = DataMethodStatic(11, 8, 2020)
print(data_1)

# Como fosse segundo construtor
data_2 = DataMethodStatic.data_string("11-08-2020")
print(data_2)

# Acessar o metodo static
# São duas formas
#   Pela instancia 
#   Chamada direta da classe
print(DataMethodStatic.data_valida("11-08-2020"))
# ou
# Depois de criar uma instancia
print(data_2.data_valida("111-08-2020"))