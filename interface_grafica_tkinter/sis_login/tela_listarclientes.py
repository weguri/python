from interface_grafica_tkinter.sis_login.conexao import ConexaoDB
from tkinter import *

try:
    cn = ConexaoDB()
    conn = cn.conexao()
    c = conn.cursor()

    try:
        sql = """ select 
                        id_clientes, nome_clientes, telefone_clientes, email_clientes
                    from clientes order by nome_clientes; """
        c.execute(sql)
        rs = c.fetchall()

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

    except:
        raise Exception("Erro!")
    finally:
        c.close()
        conn.close()

except Exception as err:
    print("Erro:", err)
finally:
    mainloop()
