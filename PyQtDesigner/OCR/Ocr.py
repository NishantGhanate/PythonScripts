from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import  QIcon ,QPixmap 
import sys
import os 
import re
import cv2
import pytesseract
# set file path 


#Init PythonUI MainWindow 
class Ocr(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ocr,self).__init__()
        pytesseract.pytesseract.tesseract_cmd = 'H:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        filePath = self.scriptDir + os.path.sep + 'ocrUI.ui'
        filePath = os.path.join(os.path.dirname(sys.executable), filePath)
        uic.loadUi(filePath,self)
        self.setWindowTitle('OCR')
        self.buttonGetImage.clicked.connect(self.getImage) 
        self.buttonExtractText.clicked.connect(self.extractText) 
        self.buttonExtractText.setEnabled(False)
    QtCore.pyqtSlot()

    def getImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open an image", "","All Files (*);;Python Files (*.py)", options=options)
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
        self.textBrowser.append(text)
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ocr = Ocr()
    ocr.show()

    sys.exit(app.exec_())
