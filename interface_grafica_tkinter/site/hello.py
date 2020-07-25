import tkinter as tk

class Application(tk.Frame):
    """
    Exemplo basico do Tkinter
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btnOla = tk.Button(self)
        self.btnOla["text"] = "Olá Mundo\n(clique em mim)"
        self.btnOla["command"] = self.digaOi
        self.btnOla.pack(side="top")

        self.quit = tk.Button(self, text="SAIR", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def digaOi(self):
        print("olá pessoal!")

root = tk.Tk()
app = Application(master=root)

# Tamanho tela
app.master.geometry("500x300")

# O maximo que pode redimencionar a Janela
app.master.maxsize(600, 300)

app.mainloop()

help(app)