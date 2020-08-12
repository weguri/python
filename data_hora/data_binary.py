from datetime import datetime

"""
Converte a data atual para binary
"""

data = bin(int(datetime.now().timestamp()))

# 
datetime.fromtimestamp(int(data, 2))
