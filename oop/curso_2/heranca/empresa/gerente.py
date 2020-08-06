from oop.curso_2.heranca.empresa.funcionario import Funcionario


class Gerente(Funcionario):
    
    def getBonificacao(self) -> float:
        """ 
        Sobrescrever o metodo da classe pai
        """
        # return self.salario * 0.10 + 1000.00
        return super().getBonificacao() + 1000.00

