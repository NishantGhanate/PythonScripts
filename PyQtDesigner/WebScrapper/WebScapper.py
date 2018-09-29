from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon
import os
import sys

class Web(QtWidgets.QMainWindow):
    def __init__(self):
        super(Web,self).__init__()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(scriptDir + os.path.sep + 'WebScrapper.ui',self)
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'python-logo.png')) 
        self.setWindowTitle('WebScrapper by [@Nishant Ghanate]') 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    web = Web()
    web.show()
    sys.exit(app.exec_())
