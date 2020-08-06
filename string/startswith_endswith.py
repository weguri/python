nomearquivo = 'frases.txt'
url = 'http://www.python.org'

# Localiza no final se termina com .txt
print(
    nomearquivo.endswith('.txt')
)

# Verifica o inicio neste caso reorna FALSE
print(
    nomearquivo.startswith('letr'),
    url.startswith('http'),
    sep="\n"
)
