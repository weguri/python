frase = "Diga-me algo."
frase += "\n\tInformação importante: "

mensagem = input(frase)
print("\tSua mensagem:", mensagem)


idade = input("\nQuantos anos você tem? ")
# print(idade >= 18)  # Traceback: TypeError, erro ocorre pois idade é do tipo str
print("\t", int(idade) >= 18)
