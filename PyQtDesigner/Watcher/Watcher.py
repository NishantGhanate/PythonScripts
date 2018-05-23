import sys
import os 
import cv2

import firebase_admin
from firebase_admin import credentials , db , firestore , storage

from PyQt5 import QtCore, QtGui, QtWidgets , uic 
from PyQt5.QtGui import QImage ,QPixmap , QIcon



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
        """ db = firestore.client()
        doc_ref = db.collection(u'users').document(u'Marvel')
        doc_ref.set({
        u'first': u'Watcher',
        u'last': u'-',
        u'born': 1
        }) """
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
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
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
        
        self.firebase = FireBase()

    QtCore.pyqtSlot()
    def activate_watcher_button(self):
        print('Watcher Activated')
        """ self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,500)
        while(1):
            ret,self.img = self.capture.read()
            #The image is stored using a 24-bit RGB format (8-8-8).
            qformat = QImage.Format_RGB888
            # img.shape[1] = col, [0] = row
            outImage = QImage(img,img.shape[1],img.shape[0],img.shape[0],qformat)
            # BGR2RGB
            outImage = outimage.rgbSwapped()
            self.labelWebCamera.setPixmap(QPixmap.fromImage(outImage))
            self.labelWebCamera.setScaledContents(True) """

    def sleep_watcher_button(self):
        print('Watching in silent mode always there for help')
        # self.capture.release()

    def save_logs_button(self):
        """ file = open('H:/Github/PythonScripts/PyQtDesigner/Watcher/Logs.txt','a+')
        file.write('This is a test') 
        file.write('To add more lines')
        file.close() """

        self.firebase.updateLog()
        self.listWidgetLogs.addItem("a")
        print('Logs saved Sucessfully')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    watch = WatcherUI()
    watch.show()
    sys.exit(app.exec_())

