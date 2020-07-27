import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# criar o aplicativo
myapp = App()

#
# aqui estão chamadas de método para a classe do gerenciador de janelas
#
myapp.master.title("My Do-Nothing Application")
myapp.master.geometry("500x300")
myapp.master.maxsize(1000, 400)

# iniciar o programa
myapp.mainloop()
