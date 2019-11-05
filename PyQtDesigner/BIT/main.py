import os
import sys
import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon

from packages.Plots import Plots

from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pylab as plt

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


class Bit(QtWidgets.QMainWindow):

    def __init__(self):
        super(Bit,self).__init__()
        uiPath = SCRIPT_DIR + os.path.sep + 'assets' + os.path.sep + 'bit.ui'
        iconPath = SCRIPT_DIR + os.path.sep + 'assets' + os.path.sep + 'icon.pnh'
        uic.loadUi(uiPath,self)
        self.setWindowTitle('Business Inteligence tool')
        # self.setWindowIcon(QIcon(iconPath)) 
        self.pushButtonOpenFile.clicked.connect(self.openFile)
        self.pushButtonBoxPlot.clicked.connect(self.boxPlot)

    def openFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open csv file", '',"Csv Files (*.csv)", options=options)
        self.df = pd.read_csv(self.fileName)
        row , col = self.df.shape
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(col)
        headers = self.df[self.df.columns[0:]]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for i in range(row):
            for j in range(col):
                x = str(self.df.iloc[i,j])
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(x))
        # info = str(self.df.info())
        # self.listWidget.addItem(info) 
    

    def boxPlot(self):
        # data = np.array([0.7,0.7,0.7,0.8,0.9,0.9,1.5,1.5,1.5,1.5])        
        # fig = Plots.boxPlot(data)
        
        data = np.array([0.7,0.7,0.7,0.8,0.9,0.9,1.5,1.5,1.5,1.5])        
        fig, ax1 = plt.subplots()
        bins = np.arange(0.6, 1.62, 0.02)
        n1, bins1, patches1 = ax1.hist(data, bins, alpha=0.6, density=False, cumulative=False)
        # plot
        self.plotWidget = FigureCanvas(fig)
        # QWidget to plot matplot graph
        lay = QtWidgets.QVBoxLayout(self.widgetPlot)  
        lay.setContentsMargins(0, 0, 0, 0)      
        lay.addWidget(self.plotWidget)
        self.addToolBar(QtCore.Qt.RightToolBarArea, NavigationToolbar(self.plotWidget, self))
        





if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    bit = Bit()
    bit.show()
    sys.exit(app.exec_())


