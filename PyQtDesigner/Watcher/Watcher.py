import sys
from PyQt5 import QtCore, QtGui, QtWidgets , uic


class WatcherUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(WatcherUI,self).__init__()
        uic.loadUi('H:/Github/PythonScripts/PyQtDesigner/Watcher/WatcherUI.ui',self)
        #self.setFixedSize(500, 500)
        # self.setWindowIcon()
        self.setWindowTitle('Watcher') 
        self.startButton.clicked.connect(self.activate_watcher_button)
        self.stopButton.clicked.connect(self.sleep_watcher_button)
        self.saveLogsButton.clicked.connect(self.save_logs_button)
        self.listWidgetLogs.addItem("a")

    QtCore.pyqtSlot()
    def activate_watcher_button(self):
        print('Watcher Activated')
    
    def sleep_watcher_button(self):
        print('Watching in silent mode always there for help')

    def save_logs_button(self):
        file = open('H:/Github/PythonScripts/PyQtDesigner/Watcher/Logs.txt','a+')
        file.write('This is a test') 
        file.write('To add more lines')
        file.close()
        print('Logs saved Sucessfully')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    watch = WatcherUI()
    watch.show()
    sys.exit(app.exec_())

