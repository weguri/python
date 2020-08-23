cobertura_disponivel = ['cogumelos', 'azeitonas', 'pimentão verde', 'calabresa', 'abacaxi', 'queijo extra']
coberturas_solicitadas = ['batatas fritas', 'cogumelos', 'queijo extra']

for coberturas_solicitada in coberturas_solicitadas:
    if coberturas_solicitada in cobertura_disponivel:
        print("Adicionando", coberturas_solicitada)
    else:
        print("Desculpe, não temos", coberturas_solicitada)

print("\nTerminei de fazer sua pizza")
