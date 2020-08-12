import re

""" 
O metodo split() aceita somente um delimitador para separar a string

Usar o modulo re
"""

texto = 'asdf fdsa; werwt, sdfh,pqpqp,     ftses'

# Somente um delimitador
print(texto.split(";"))

# Múltiplos delimitadores
#   Os delimitadores não faram parte do retorno dos dados
txt_re = re.split(r'[;,\s]\s*', texto)
print(txt_re)


# Mantem os delimitadores
txt_re = re.split(r'(;|,|\s)\s*', texto)
print(txt_re)


# txt_re = re.split(r'(?:,|;|\s)\s*', texto)
# print(txt_re)
