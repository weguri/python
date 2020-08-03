from tkinter import *

Label(text="Cadastro de Pessoas", anchor=W, justify=CENTER,
      font=("Arial", 20)).grid(row=1, column=1, columnspan=4, pady=5)

camposPessoa = ("Nome", "Fone", "E-mail", "RG", "CPF", "Data", "OBS")

linha = 2
g = globals()

for campo in camposPessoa:
    Label(text=campo, anchor=W, justify=LEFT).grid(row=linha, column=1, pady=5)

    Entry().grid(row=linha, column=2, pady=5, padx=5)

    linha += 1


btnGravar = Button(text="Gravar")
btnGravar.grid(row=linha + 1, column=1, pady=5, padx=5)



mainloop()
