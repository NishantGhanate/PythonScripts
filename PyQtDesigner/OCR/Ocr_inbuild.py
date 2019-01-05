# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os , re , cv2 , pytesseract
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QIcon ,QPixmap 

class Ui_MainWindow(object):

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'H:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'

    def setupUi(self, MainWindow):
        # window = QtWidgets.QMainWindow()
        # window.setWindowTitle('PictureWorkshop')

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1158, 719)
        MainWindow.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"    background-color:rgb(72,164,136);\n"
"    /*background-image: url(\'H:/Github/PythonScripts/PyQtDesigner/WebScrapper/bg.png\');*/\n"
"     background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat;\n"  
"}\n"
"\n"
"\n"
"\n"
"QLabel\n"
"{    \n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: black;\n"
"      border-width: 1px 1px 1px 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonGetImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetImage.setGeometry(QtCore.QRect(30, 620, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonGetImage.setFont(font)
        self.buttonGetImage.setObjectName("buttonGetImage")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(30, 50, 711, 521))
        self.labelImage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.buttonExtractText = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText.setGeometry(QtCore.QRect(190, 620, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonExtractText.setFont(font)
        self.buttonExtractText.setObjectName("buttonExtractText")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(860, 620, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonClear.setFont(font)
        self.buttonClear.setObjectName("buttonClear")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(1030, 620, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(860, 50, 451, 521))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1158, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonGetImage.clicked.connect(self.getImage) 
        self.buttonExtractText.clicked.connect(self.extractText) 
        self.buttonExtractText.setEnabled(False)
        self.buttonClear.clicked.connect(self.clearText) 
        self.buttonSave.clicked.connect(self.saveText) 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Optical Character Recognition"))
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'ocrLogo.png'))
        self.buttonGetImage.setText(_translate("MainWindow", "Load image"))
        self.buttonExtractText.setText(_translate("MainWindow", "Extract text"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))

    
    def getImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(options=options)
        # self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open a image", "","All Files (*);;Image Files (*.jpg);;Image Files (*.png)", options=options)
        if self.fileName:
            print(self.fileName)
            pattern = ".(jpg|png|jpeg|bmp|jpe|tiff)$"
            if re.search(pattern,self.fileName):
                self.setImage(self.fileName)

    def setImage(self,fileName):
        self.labelImage.setPixmap(QPixmap(fileName))
        self.buttonExtractText.setEnabled(True)
    
    def extractText(self):
        config = ('-l eng --oem 1 --psm 3')
        img = cv2.imread(self.fileName, cv2.IMREAD_COLOR)
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(img, config=config)
        # Print recognized text
        self.textEdit.append(text)
        print(text)

    def clearText(self):
        self.textEdit.clear()

    def saveText(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        # fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save text","All Files (*);;Text Files (*.txt)", options=options)
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(options=options)
        if fileName:
            print(fileName)
            file = open(fileName,'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

