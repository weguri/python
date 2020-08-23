"""
Exemplo de como utilizar o import e from
"""
# Exemplo 1
import defs.numeros_arbitrario_argumentos
defs.numeros_arbitrario_argumentos.fazer_pizza('cogumelos', 'pimentão verde', 'queijo extra')

# Exemplo 2
import defs.numeros_arbitrario_argumentos as pz
pz.fazer_pizza('cogumelos', 'pimentão verde', 'queijo extra')

# Exemplo 3
from defs.numeros_arbitrario_argumentos import fazer_pizza
fazer_pizza('cogumelos', 'pimentão verde', 'queijo extra')

# Exemplo 4
from defs.numeros_arbitrario_argumentos import fazer_pizza as p
p('cogumelos', 'pimentão verde', 'queijo extra')

# Exemplo 5
from defs.numeros_arbitrario_argumentos import *
fazer_pizza('cogumelos', 'pimentão verde', 'queijo extra')