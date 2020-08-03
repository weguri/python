import sys

from PyQt5.uic.properties import QtGui


class Main(QtGui.QWidget):
    def __init__(self, master=None):
        QtGui.QWidget.__init__(self, master)
        self.setGeometry(400, 300, 250, 250)

        self.setWindowTitle("Titulo para exibir")


app = QtGui.QApplication(sys.argv)
programa = Main()
programa.show()

sys.exit(app.exec_())
