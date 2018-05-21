import sys
from PyQt5 import QtGui

class Window(QtGui.ma):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('python-logo.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())