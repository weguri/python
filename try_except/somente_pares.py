"""
Herança:
    A classe SomentePares HERDA classe list

sobrescrever(overwrite)
    metodo: append
"""


class SomentePares(list):
    
    # sobrescrever o metodo
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Somente inteiro")
        if value % 2:
            raise ValueError("Somente Pares")
        
        """ Apos validar a informação acrescente na lista """
        super().append(value)


""" Exemplo de uso """
sp = SomentePares()
# 
# Retorna: TypeError
# sp.append("Texto")
#  
# Retorna: ValueError
# sp.append(5)
# Somente valor PAR


sp.append(10)
sp.append(2)
sp.append(6)
sp.append(12)
print(sp)

