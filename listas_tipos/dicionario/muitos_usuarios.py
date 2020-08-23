"""
Dicionário em um dicionário
    Podemos aninhar um dicionário em outro dicionário
"""

usuarios = {
    'alberteinstein': {
        'nome': 'albert',
        'sobrenome': 'einstein',
        'pais': 'alemanha'
    },
    'stephenhawking': {
        'nome': 'stephen',
        'sobrenome': 'hawking',
        'pais': 'reino unido'
    }
}

for username, info_user in usuarios.items():
    print("\nUsuario:", username)
    
    nome_completo = info_user['nome'] + " " + info_user['sobrenome']
    localizacao = info_user['pais']

    print("\tNome:", nome_completo.title())
    print("\tPais:", localizacao.title())
