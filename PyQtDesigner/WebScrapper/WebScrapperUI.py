# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\Github\PythonScripts\PyQtDesigner\WebScrapper\WebScrapper.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import  QSystemTrayIcon, QAction 
from PyQt5.QtGui import  QIcon
from datetime import datetime
from requests_html import HTMLSession
import requests.exceptions 
import os
import sys
import multiprocessing

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setWindowTitle('WebScrapper by [@Nishant Ghanate]')
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'icon.png')) 
        
        # Gui.QSystemTrayIcon
        MainWindow.setAutoFillBackground(False)
        # MainWindow.setMaximumWidth(1366)
        # MainWindow.setMaximumHeight(768)
        MainWindow.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"    /*background-color:rgb(195,223,255);*/\n"
"    background-image: url(\'H:/Github/PythonScripts/PyQtDesigner/WebScrapper/bg.png\');\n"
"     background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat;\n"
"    "
"              \n"
"    \n"
"}\n"
"\n"
"\n"
"QWidget#centralwidget\n"
"{\n"
"\n"
"}\n"
"\n"
"QLabel\n"
"{    \n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"")     
        # self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'icon.png')) 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidgetMain = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetMain.setGeometry(QtCore.QRect(30, 60, 481, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidgetMain.setFont(font)
        self.listWidgetMain.setObjectName("listWidgetMain")
        self.listWidgetLogs = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetLogs.setGeometry(QtCore.QRect(860, 60, 461, 541))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidgetLogs.setFont(font)
        self.listWidgetLogs.setObjectName("listWidgetLogs")
        self.buttonGetInput = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetInput.setGeometry(QtCore.QRect(40, 630, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonGetInput.setFont(font)
        self.buttonGetInput.setObjectName("buttonGetInput")
        self.textEditUrl = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditUrl.setGeometry(QtCore.QRect(30, 490, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditUrl.setFont(font)
        self.textEditUrl.setObjectName("textEditUrl")
        self.textEditSource = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSource.setGeometry(QtCore.QRect(30, 570, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditSource.setFont(font)
        self.textEditSource.setObjectName("textEditSource")
        self.buttonClearLogs = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClearLogs.setGeometry(QtCore.QRect(980, 630, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonClearLogs.setFont(font)
        self.buttonClearLogs.setObjectName("buttonClearLogs")
        self.buttonSaveLogs = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSaveLogs.setGeometry(QtCore.QRect(860, 630, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonSaveLogs.setFont(font)
        self.buttonSaveLogs.setObjectName("buttonSaveLogs")
        self.radioButtonFirst = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonFirst.setGeometry(QtCore.QRect(120, 540, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonFirst.setFont(font)
        self.radioButtonFirst.setObjectName("radioButtonFirst")
        self.buttonStop = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(150, 630, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonStop.setFont(font)
        self.buttonStop.setObjectName("buttonStop")
        self.radioButtonAll = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonAll.setGeometry(QtCore.QRect(230, 540, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonAll.setFont(font)
        self.radioButtonAll.setObjectName("radioButtonAll")
        self.labelMain = QtWidgets.QLabel(self.centralwidget)
        self.labelMain.setGeometry(QtCore.QRect(170, 20, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMain.setFont(font)
        self.labelMain.setAutoFillBackground(False)
        self.labelMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelMain.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelMain.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMain.setObjectName("labelMain")
        self.labelLog = QtWidgets.QLabel(self.centralwidget)
        self.labelLog.setGeometry(QtCore.QRect(1000, 20, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLog.setFont(font)
        self.labelLog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelLog.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelLog.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLog.setObjectName("labelLog")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 470, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 540, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(260, 630, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonClear.setFont(font)
        self.buttonClear.setObjectName("buttonClear")
        MainWindow.setCentralWidget(self.centralwidget)
           
        # self.setFixedSize(1366, 768)
        self.buttonGetInput.clicked.connect(self.getInput)
        self.buttonSaveLogs.clicked.connect(self.saveLogs)
        self.buttonClearLogs.clicked.connect(self.clearLogs)
        self.buttonClear.clicked.connect(self.clear)
        self.buttonStop.clicked.connect(self.stop)
        self.buttonStop.setEnabled(False)
        self.oldUrl = "_"
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonGetInput.setText(_translate("MainWindow", "Get "))
        self.buttonClearLogs.setText(_translate("MainWindow", "Clear logs"))
        self.buttonSaveLogs.setText(_translate("MainWindow", "Save Logs"))
        self.radioButtonFirst.setText(_translate("MainWindow", "Firs page"))
        self.buttonStop.setText(_translate("MainWindow", "Stop"))
        self.radioButtonAll.setText(_translate("MainWindow", "All pages"))
        self.labelMain.setText(_translate("MainWindow", "Command Logs"))
        self.labelLog.setText(_translate("MainWindow", "Source logs"))
        self.label.setText(_translate("MainWindow", "Website url :"))
        self.label_2.setText(_translate("MainWindow", "Xpath  :"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.Stop = True

    #Acttivate UI fucntions
    # QtCore.pyqtSlot()

    # Returns Time in e.g 1 oct 2018 formart
    def getTimeStamp(self):
        return  datetime.now().strftime("%A %d. %B %Y %I:%M:%S %p")

    def stop(self):
        self.buttonGetInput.setEnabled(True)
        self.Stop = False
    
    # Validate input url and throw Expection for invalid
    def validateUrl(self,url):
        try:
            # Create new session only if new url 
            if self.oldUrl != url:
                self.oldUrl = url
                session = HTMLSession()
                self.r = session.get(url)
                return True
            # else True because if only xpathSrc changed and continue scrapping from given url
            else :
                return True
        # Throw expection and close the fucntion 
        except requests.exceptions.RequestException  as e:
            self.listWidgetLogs.addItem(str(e))
            return False
    
      # This function will scrap it is also recurive if required 
    def getSource(self):
        try:  
            # returns list for single Xpath item 
            src = self.r.html.xpath(self.xpathSrc)
            # proceed further if list is not empty
            if src  and self.Stop :
                timeStamp = self.getTimeStamp()
                for s in src:
                    # print(s)
                    s = str(s)
                    # List widget only supports string
                    self.listWidgetLogs.addItem(s)
                    # if all pages is checked
                if  self.radioButtonAll.isChecked():
                    if self.r.html._next():
                        print(self.r.html._next())
                        url = self.validateUrl(self.r.html._next())
                        if url and  self.r.status_code == 200:
                            # self.listWidgetLogs.addItem('\n'+self.r.html._next())
                            self.getSource()     
        except :
            self.listWidgetLogs.addItem('invalid xpath format')


      # Get button function connection  
    def getInput(self):
        url = self.textEditUrl.toPlainText()
        self.xpathSrc = self.textEditSource.toPlainText()
        print(self.xpathSrc)
        if url and self.xpathSrc.strip() :
            source = self.validateUrl(url)
            if source:
                timestampDay = self.getTimeStamp()
                self.listWidgetLogs.addItem(timestampDay)
                self.listWidgetMain.addItem(self.xpathSrc)
                self.getSource()
                self.buttonStop.setEnabled(True)
              

        elif url is None or len(url) < 5:
            timestampDay = self.getTimeStamp()
            self.listWidgetLogs.addItem(timestampDay)
            self.listWidgetLogs.addItem('Url cannot be empty ')
        else :
            timestampDay = self.getTimeStamp()
            self.listWidgetLogs.addItem(timestampDay)
            self.listWidgetLogs.addItem('xpath input  where is it ?')
    
     # Saves logs from Preserved logs
    def saveLogs(self):
        timestampDay =  datetime.now().strftime("%A %d %B %Y %I %M %S%p")
        fileName = self.scriptDir + os.path.sep +'WebScrappingLogs '+ timestampDay +'.txt'
        file = open(fileName,'a+' , encoding='utf-8')
        
        file.writelines('Command Logs ' + timestampDay + '\n')
        for i in range(self.listWidgetMain.count()):
            file.writelines(self.listWidgetMain.item(i).text() + '\n')

        file.writelines('\nSource Logs')
        for i in range(self.listWidgetLogs.count()):
            file.writelines(self.listWidgetLogs.item(i).text() + '\n')
        # file.writelines(itemsTextList)
        file.close()
        self.listWidgetLogs.addItem('Logs saved Sucessfully')
    
    # clear preservedLogs      
    def clearLogs(self):
        self.listWidgetLogs.clear()

    def clear(self):
        self.listWidgetMain.clear()




if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
   
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('WebScrapper by [@Nishant Ghanate]')
    MainWindow.show()
    
    sys.exit(app.exec_())

