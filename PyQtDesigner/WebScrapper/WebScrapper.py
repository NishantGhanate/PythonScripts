from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon
from datetime import datetime
from requests_html import HTMLSession

import requests.exceptions 
import os
import sys
import multiprocessing



class Guide(QtWidgets.QWidget):
     def __init__(self):
        super(Guide,self).__init__()
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(self.scriptDir + os.path.sep + 'Guide.ui',self)
        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'icon.png')) 
        self.setWindowTitle('Guide for Webscraping') 



#Init PythonUI MainWindow 
class Web(QtWidgets.QMainWindow):
    def __init__(self):
        super(Web,self).__init__()
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        filePath = self.scriptDir + os.path.sep + 'WebScrapper.ui'
        filePath = os.path.join(os.path.dirname(sys.executable), filePath)
        uic.loadUi(filePath,self)
        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'icon.png')) 
        self.setWindowTitle('WebScrapper by [@Nishant Ghanate]') 
        # self.setFixedSize(1366, 768)
        self.buttonGetInput.clicked.connect(self.getInput)
        self.buttonSaveLogs.clicked.connect(self.saveLogs)
        self.buttonClearLogs.clicked.connect(self.clearLogs)
        self.buttonClear.clicked.connect(self.clear)
        self.buttonStop.clicked.connect(self.stop)
        self.buttonStop.setEnabled(False)
        self.oldUrl = "_"
        self.Guide = Guide()
        self.actionGuide.triggered.connect(self.guideWindow)

    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    #Acttivate UI fucntions
    QtCore.pyqtSlot()
    
    # Returns Time in e.g 1 oct 2018 formart
    def getTimeStamp(self):
        return  datetime.now().strftime("%A %d. %B %Y %I:%M:%S %p")

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

    def stop(self):
        self.processGetSource.terminate()
        print ('Process terminated:', self.processGetSource, self.processGetSource.is_alive())
        self.buttonGetInput.setEnabled(True)

    # This function will scrap it is also recurive if required 
    def getSource(self):
        try:  
            # returns list for single Xpath item 
            src = self.r.html.xpath(self.xpathSrc)
            # proceed further if list is not empty
            if src :
                self.buttonGetInput.setEnabled(False)
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
            self.listWidgetLogs.addItem('Xpath exception please try again')
           
    
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
                self.processGetSource = multiprocessing.Process(target=self.getSource())
                self.processGetSource.start()
                self.processGetSource.join()
                self.buttonGetInput.setEnabled(False)
                print ('Process joined:', self.processGetSource, self.processGetSource.is_alive())
                print ('Process exit code:', self.processGetSource.exitcode)
                if self.processGetSource.exitcode == 0:
                    self.buttonStop.setEnabled(False)
                    self.stop()
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

    # Open Guide window froms status bar
    def guideWindow(self):
        self.Guide.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    web = Web()
    web.show()

    sys.exit(app.exec_())


