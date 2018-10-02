from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon
from datetime import datetime
from requests_html import HTMLSession
from requests.exceptions import ConnectionError
import os
import sys

class Web(QtWidgets.QMainWindow):
    def __init__(self):
        super(Web,self).__init__()
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(self.scriptDir + os.path.sep + 'WebScrapper.ui',self)
        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'icon.png')) 
        self.setWindowTitle('WebScrapper by [@Nishant Ghanate]') 
        self.buttonLoadUrl.clicked.connect(self.getUrl)
        self.buttonGetSource.clicked.connect(self.getSource)
        self.buttonGetSource.setEnabled(False)
        self.buttonSaveLogs.clicked.connect(self.saveLogs)
        self.buttonClearLogs.clicked.connect(self.clearLogs)
    
    QtCore.pyqtSlot()

    def getUrl(self):
        url = self.textEditUrl.toPlainText()
        session = HTMLSession()
        try:
            self.r = session.get(url)
        except ConnectionError as e:
            print(e)
            sys.exit(1)
        print(self.r.status_code)
        if self.r.status_code ==200:
            self.listWidgetLogs.addItem(str(self.r.status_code))
            self.buttonGetSource.setEnabled(True)
        else:
            self.listWidgetLogs.addItem(str(self.r.status_code))
            # sys.exit(1)
            

    def getSource(self):
        src = self.textEditSource.toPlainText()
        # print(src)
        try:
            r = self.r.html.xpath(src)
            # timestampDay =  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")
            # self.listWidgetLogs.addItem(timestampDay)
            # print(type(r))
            for _ in r:
                print(_)
                _ = str(_)
                self.listWidgetLogs.addItem(_)
        except:
            self.listWidgetLogs.addItem('Something went wrong ops!')
    

    
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