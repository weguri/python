from tkinter import Tk
from interface_grafica_tkinter.sis_login.login import Login

main = Tk()
tela = Login(main)
main.geometry("320x110+500+200")
main.mainloop()
