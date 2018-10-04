from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon
from datetime import datetime
from requests_html import HTMLSession
import requests.exceptions 
import os
import sys

#Init PythonUI 
class Web(QtWidgets.QMainWindow):
    def __init__(self):
        super(Web,self).__init__()
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(self.scriptDir + os.path.sep + 'WebScrapper.ui',self)
        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'icon.png')) 
        self.setWindowTitle('WebScrapper by [@Nishant Ghanate]') 
        self.buttonGetInput.clicked.connect(self.getInput)
        self.buttonSaveLogs.clicked.connect(self.saveLogs)
        self.buttonClearLogs.clicked.connect(self.clearLogs)
        # self.buttonClear.clicked.connect()
        # self.buttonStop.clicked.connect()

        self.oldUrl = "_"

    #Acttivate UI fucntions
    QtCore.pyqtSlot()

    # Returns Time in e.g 1 oct 2018 formart
    def getTimeStamp(self):
        return  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")

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
        # returns list for single Xpath item 
        src = self.r.html.xpath(self.xpathSrc)
        # proceed further if list is not empty
        if src :
            timeStamp = self.getTimeStamp()
            for s in src:
                print(s)
                s = str(s)
                # List widget only supports string
                self.listWidgetLogs.addItem(s)
            
            if self.r.html._next():
                print(self.r.html._next())
                url = self.validateUrl(self.r.html._next())
                if url:
                    if self.r.status_code == 200:
                        self.getSource()   
        

    # Get button function connection  
    def getInput(self):
        url = self.textEditUrl.toPlainText()
        self.xpathSrc = self.textEditSource.toPlainText()

        if url and self.xpathSrc is not None:
            source = self.validateUrl(url)
            if source:
                self.getSource()
        elif url is None or len(url) < 5:
            timestampDay = self.getTimeStamp()
            self.listWidgetLogs.addItem(timestampDay)
            self.listWidgetLogs.addItem('Url cannot be empty ¯\_(ツ)_/¯ \n')
        elif self.xpathSrc is None:
            self.listWidgetLogs.addItem('xpath input \_(ʘ_ʘ)_/ ? ')
           
    # Saves logs from Preserved logs
    def saveLogs(self):
        timestampDay =  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")
        file = open(self.scriptDir + os.path.sep +'WebScrappingLogs_'+timestampDay+'.txt','a+')
        i = 0
        for log in self.listWidgetLogs.item(i).text():
            file.write(log +'\n')
            i += 1
        file.close()
        self.listWidgetLogs.addItem('Logs saved Sucessfully')
    
     # clear preservedLogs      
    def clearLogs(self):
        self.listWidgetLogs.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    web = Web()
    web.show()
    sys.exit(app.exec_())

# https://www.reddit.com/r/ProgrammerHumor/
# r = r.html.xpath('//*[@class="y8HYJ-y_lTUHkQIc1mdCq"]//h2//text()')
