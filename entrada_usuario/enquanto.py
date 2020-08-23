frase = "Diga-me algo."
frase += "\n\tPara fechar digite sair: "

mensagem = ""
while mensagem != 'sair':
    mensagem = input(frase)

    if mensagem.lower() != 'sair':
        print("\tMensagem:", mensagem, end="\n\n")

#
# enquanto variavel for verdadeiro
print('\n', '-' * 11, "While variavel true", '-' * 11)
active = True
while active:
    mensagem = input(frase)
    if mensagem == 'sair':
        active = False
    else:
        print("\tMensagem:", mensagem, end="\n\n")

#
# while True: break
print('\n', '-' * 11, "while True: break", '-' * 11)
while True:
    mensagem = input(frase)
    if mensagem == 'sair':
        break

    print("\tMensagem:", mensagem, end="\n\n")
