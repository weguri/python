from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # aqui é a variável da aplicação
        self.contents = StringVar()
        # defina-o com algum valor
        self.contents.set("this is a variable")
        # diga ao widget de entrada para assistir essa variável
        self.entrythingy["textvariable"] = self.contents

        # e aqui recebemos um retorno de chamada quando o usuário clicar em retornar.
        # teremos o programa imprimindo o valor do
        # variável de aplicativo quando o usuário acessa return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())

# crie o aplicativo
myapp = App()

#
# aqui estão chamadas de método para a classe do gerenciador de janelas
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# iniciar o programa
myapp.mainloop()