from include.conexao import ConexaoDB
from tkinter import *

try:
    Label(text="Lista de Pessoas", font=("Arial", 15)).grid(
        row=1, column=1, columnspan=4, pady=5)
    Label(text="Código", relief=RIDGE, width=7,
          bg="dark grey").grid(row=2, column=1)
    Label(text="Nome", relief=RIDGE, width=30,
          bg="dark grey").grid(row=2, column=2)
    Label(text="Telefone", relief=RIDGE, width=15,
          bg="dark grey").grid(row=2, column=3)
    Label(text="E-mail", relief=RIDGE, width=30,
          bg="dark grey").grid(row=2, column=4)

    conn = ConexaoDB().conexao()
    cursor = conn.cursor()

    sql = """ select 
                    id_clientes, nome_clientes, telefone_clientes, email_clientes
                from clientes order by nome_clientes; """
    cursor.execute(sql)
    rs = cursor.fetchall()

    numPess = len(rs)

    contRow = 2
    for linha in rs:
        codigo = linha[0]
        nome = linha[1]
        fone = linha[2]
        email = linha[3]

        corRow = "white"
        if contRow % 2 == 0:
            corRow = "light gray"

        Label(text=codigo, relief=RIDGE, width=7,
              bg=corRow).grid(row=contRow + 1, column=1)
        Label(text=nome, relief=RIDGE, width=30, bg=corRow,
              anchor=W).grid(row=contRow + 1, column=2)
        Label(text=fone, relief=RIDGE, width=15, bg=corRow).grid(
            row=contRow + 1, column=3)
        Label(text=email, relief=RIDGE, width=30,
              bg=corRow, anchor=E).grid(row=contRow + 1, column=4)
        contRow += 1

    qtdPessoas = ("Total de %d clientes" % numPess)
    Label(text=qtdPessoas, anchor=W).grid(
        row=contRow+1, column=1, columnspan=4, pady=5)


except Exception as err:
    print("Erro:", err)
else:
    cursor.close()
    conn.close()
finally:
    mainloop()
