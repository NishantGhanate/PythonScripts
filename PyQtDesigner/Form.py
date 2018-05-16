import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setWindowTitle("Logs")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.pushButton.setObjectName("push button")
        self.pushButton.setText( "Hello World")
        self.pushButton.clicked.connect(self.output)
        self.pushButton.resize(self.pushButton.minimumSizeHint())
        #self.pushButton.move(0,0)
        #self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def output(self):
        print("whooaaaa  Hellow world once again!!!")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Python GUI"))
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton.setText(_translate("Form", "Hello world"))
        self.pushButton.resize(100,50)
        self.pushButton.move(100,100)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())