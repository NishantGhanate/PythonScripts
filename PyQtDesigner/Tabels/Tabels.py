# just for future references , how to perfom crud on tables in pyqt5

from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon
from PyQt5.QtCore import QTimer , QThreadPool , QThread , pyqtSignal , QObject
from PyQt5.QtWidgets import QSizePolicy , QGridLayout , QTableWidgetItem , QAction , QMessageBox
from datetime import datetime
import os,sys,csv


class NewThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(int, list)
    labelSignal = QtCore.pyqtSignal(str)
    def __init__(self):
        QtCore.QThread.__init__(self)
        self._tableCounter = 0

    def updateTable(self):
        for i in range(10):
            self.signal.emit(self._tableCounter, [i,i,i])
            self._tableCounter += 1

    def run(self):
        self.updateTable()


class Tabels(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Tabels, self).__init__(*args, **kwargs)
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(self.scriptDir + os.path.sep +  'Assests' + os.path.sep +'Tabel.ui',self)
        self.setTableHeader()
        self.pushButton.clicked.connect(self.saveTable)
        self.tableWidget.cellClicked.connect(self.getTableValue)
        self.newThread = NewThread()
        self.newThread.signal.connect(self.addToTable)

    def setTableHeader(self):
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setUpdatesEnabled(True)
        self.tableWidget.blockSignals(False)
        self.Headers = ['A','B','C']
        self.tableWidget.setHorizontalHeaderLabels(self.Headers)

    
    @QtCore.pyqtSlot(int, list)    
    def addToTable(self,row, dataList):
        self.tableWidget.setRowCount(row+1)
        # print(dataList)
        for i , value in enumerate(dataList):
            item = QTableWidgetItem( str(value)) # create the item
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, i,item)
    
    def clearTable(self):
        self.tableWidget.setRowCount(0)
        self.newThread._tableCounter = 0
    
    def saveTable(self):
        fileName, done = QtWidgets.QInputDialog.getText( 
        self, 'Save file', 'Enter file name:')
        if done and fileName:  
            csvFilePath =  self.filesPath + os.path.sep + fileName + '.csv'
            rowCount = self.tableWidget.rowCount()
            columnCount = self.tableWidget.columnCount()
            with open(csvFilePath,'a' , newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(self.Headers)
                for r in range(rowCount):
                    arr = []
                    for c in range(columnCount):
                        item = self.tableWidget.item(r, c)
                        if item:
                            item = item.text()
                            arr.append(item)
                        else:
                            arr.append('')    
                    writer.writerow(arr)
            QMessageBox.about(self, "File saved ", csvFilePath)

    def getTableValue(self, row, column):
        # print("Row %d and Column %d was clicked" % (row, column))
        # item = self.tableWidget.itemAt(row, column)
        item = self.tableWidget.item(row, column)
        if not item :
            return
            
        item = item.text()    
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Information")
        msgbox.setText('Please select an option below')
        yes = msgbox.addButton(' Yes', QMessageBox.YesRole)
        maybe = msgbox.addButton('May be', QMessageBox.ActionRole)
        cancelButton = msgbox.addButton(QMessageBox.Cancel)

        bttn = msgbox.exec_()
        if msgbox.clickedButton() == yes:
            # Finally an yes 
            pass
    
        elif msgbox.clickedButton() == maybe:
            # do something else , cry in a corner may be with spagetti code
            pass

            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tabels = Tabels()
    tabels.show()
    sys.exit(app.exec_())