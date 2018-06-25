import sys
import os 
import cv2

import firebase_admin
from firebase_admin import credentials , db , firestore , storage

from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import QImage ,QPixmap , QIcon
from PyQt5.QtCore import QTimer


class FireBase():
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('H:/Github/PythonScripts/Firebase/AdminSdk.json')
        
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://pythonfirebase-449e8.firebaseio.com',
        'storageBucket': 'gs://pythonfirebase-449e8.appspot.com'
        })
      
    def updateLog(self):
       
        # ref = db.reference('/')   
        # print (ref.get() )
        db = firestore.client()
        doc_ref = db.collection(u'users').document(u'SecurityLogs')
        doc_ref.set({
        u'first': u'Watcher',
        u'last': u'-',
        u'born': 1
        })
        bucket = storage.bucket()

    def sendNotification(self):

        # This registration token comes from the client FCM SDKs.
        registration_token = 'YOUR_REGISTRATION_TOKEN'
        # See documentation on defining a message payload.
        message = messaging.Message(
        data={
        'score': '850',
        'time': '2:45',
        },
        token=registration_token,
        )
        # Send a message to the device corresponding to the provided
        response = messaging.send(message)
        print('Successfully sent message:', response)



class WatcherUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(WatcherUI,self).__init__()
        uic.loadUi('H:/Github/PythonScripts/PyQtDesigner/Watcher/MainWindowUI.ui',self)
        #self.setFixedSize(500, 500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'python-logo.png')) 
        self.setWindowTitle('Watcher') 
        self.startButton.clicked.connect(self.activate_watcher_button)
        self.stopButton.clicked.connect(self.sleep_watcher_button)
        self.saveLogsButton.clicked.connect(self.save_logs_button)
        self.stop = False
        self.firebase = FireBase()

    QtCore.pyqtSlot()

    def activate_watcher_button(self):
        print('Watcher Activated')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    
    def update_frame(self):
        ret,self.image = self.cap.read()
        self.displayImage(self.image,1)

    def displayImage(self,img,window=1):
        qformat = QImage.Format_Indexed8
        qformat = QImage.Format_RGB888
        outImage = QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)    
        outImage = outImage.rgbSwapped()
        if window ==1:
            self.labelWebCamera.setPixmap(QPixmap.fromImage(outImage))
            self.labelWebCamera.setScaledContents(True)
            

         
    def sleep_watcher_button(self):
        print('Watching in silent mode always there for help')
        self.cap.release()
        self.timer.stop()

        

        
          

    def save_logs_button(self):
        file = open('H:/Github/PythonScripts/PyQtDesigner/Watcher/Logs.txt','a+')
        file.write('This is a test') 
        file.close()
        self.firebase.updateLog()
        self.listWidgetLogs.addItem("a")
        print('Logs saved Sucessfully')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    watch = WatcherUI()
    watch.show()
    sys.exit(app.exec_())

