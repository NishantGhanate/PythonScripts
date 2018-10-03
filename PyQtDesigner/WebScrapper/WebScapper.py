from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon
from datetime import datetime
from requests_html import HTMLSession
import requests.exceptions 
import os
import sys

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
        self.oldUrl = "_"
    
    QtCore.pyqtSlot()
    def getTimeStamp(self):
        return  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")

    def validateUrl(self,url):
        try:
            # if new url found 
            if self.oldUrl != url:
                self.oldUrl = url
                session = HTMLSession()
                self.r = session.get(url)
                return True
            else :
                return False
        except requests.exceptions.RequestException  as e:
            self.listWidgetLogs.addItem(str(e))
            return False
            

    def getSource(self):
        src = self.r.html.xpath(self.xpathSrc)
        
        if src :
            timeStamp = self.getTimeStamp()
            for s in src:
                print(s)
                s = str(s)
                self.listWidgetLogs.addItem(s)
            if self.r.html._next():
                print(self.r.html._next())
                url = self.validateUrl(self.r.html._next())
                if url:
                    if self.r.status_code == 200:
                        self.getSource()   
        

        
    def getInput(self):
        url = self.textEditUrl.toPlainText()
        self.xpathSrc = self.textEditSource.toPlainText()
        if url is None or len(url) < 5:
            timestampDay = self.getTimeStamp()
            self.listWidgetLogs.addItem(timestampDay)
            self.listWidgetLogs.addItem('Url cannot be empty ¯\_(ツ)_/¯ \n')
        elif self.xpathSrc is None:
            self.listWidgetLogs.addItem('xpath input \_(ʘ_ʘ)_/ ? ')
        else :
            source = self.validateUrl(url)
            if source:
                self.getSource()
            

    def saveLogs(self):
        timestampDay =  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")
        file = open(self.scriptDir + os.path.sep +'WebScrappingLogs_'+timestampDay+'.txt','a+')
        i = 0
        for log in self.listWidgetLogs.item(i).text():
            file.write(log +'\n')
            i += 1
        file.close()
        self.listWidgetLogs.addItem('Logs saved Sucessfully')
    
           
    def clearLogs(self):
        self.listWidgetLogs.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    web = Web()
    web.show()
    sys.exit(app.exec_())

# https://www.reddit.com/r/ProgrammerHumor/
# r = r.html.xpath('//*[@class="y8HYJ-y_lTUHkQIc1mdCq"]//h2//text()')


        #    if self.r.html._next():
        #             url = validateUrl(self.r.html._next())
        #             if url:
        #                 if self.r.status_code == 200:
        #                     self.getSource()   
        #             else:
        #                 self.listWidgetLogs.addItem('Sorry we are unable to get next page')

        #     else:
        #         self.listWidgetLogs.addItem('Could not find given xpath, (•◡•) please try again diffrent')