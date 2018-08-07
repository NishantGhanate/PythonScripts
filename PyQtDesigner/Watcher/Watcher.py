import sys
import os 
import cv2
import base64
from datetime import datetime , timedelta
import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials , db , firestore , storage , messaging  

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

    def validateUid(self,uid):
        try:
            ref = db.reference('users/'+ uid)
            print(ref.get())
            if(ref.get() != None):
                self.uid = uid
                return ref.get()        
        except :
            return(None)
        


    def updateLog(self,timestampDay):   
        ref = db.reference('users/'+self.uid+'/motionLogs')
        ref.push(timestampDay)
        # print (ref.get() )
        # db = firestore.client()
        # doc_ref = db.collection(u'users').document(u'WMzLqZFN00NxwYllD9oKSMqiDuv1').collection(u'data').document(u'motionLogs')
        # data = {
        #     'time': timestamp   
        # }
        # sata = {
        #     timestamp :data   
        # }
        # doc_ref.set(sata)
        # bucket = storage.bucket()

    def sendNotification(self):
        fcmRef = db.reference('users/'+self.uid+'/fcmToken')
        fcmRef = fcmRef.get()
        # print(fcmRef)

        # This registration token comes from the client FCM SDKs.
        registration_token = fcmRef
        # See documentation on defining a message payload.
        message = messaging.Message( 
            notification= messaging.Notification(
                title='Watcher Detected motion ',
                body='Action Required ',
                ),
            android=messaging.AndroidConfig(
                ttl=timedelta(seconds=3600),
                priority='normal',
            ),     
            token=registration_token,
        )

        # Send a message to the device corresponding to the provided
        response = messaging.send(message)
        print('Successfully sent message:', response)

    def saveImage(self,image):
        images = db.reference('users/'+self.uid+'/images')
        images.push(image)



class WatcherUI(QtWidgets.QMainWindow):

    cap = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    kernel = np.ones((3,3),np.uint8)
    kernelSmooth = np.ones( (25,25),np.float32 ) / 625
    ret , frame = cap.read()
    pastFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    presentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pixelDifference = 350000
    timeCheck = datetime.now().strftime('%Ss')
    font = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self):
        super(WatcherUI,self).__init__()
        uic.loadUi('H:/Github/PythonScripts/PyQtDesigner/Watcher/MainWindowUI.ui',self)
        #self.setFixedSize(500, 500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'python-logo.png')) 
        self.setWindowTitle('Watcher') 
        self.buttonStart.clicked.connect(self.activate_watcher_button)
        self.buttonStart.setEnabled(False)
        self.buttonStop.clicked.connect(self.sleep_watcher_button)
        self.buttonStop.setEnabled(False)
        self.buttonSaveUid.clicked.connect(self.saveUid)
        self.buttonSaveLogs.clicked.connect(self.save_logs_button)
        self.stop = False
        self.firebase = FireBase()
        self.logCount = 0

    QtCore.pyqtSlot()

    def saveUid(self):
        uid = self.lineEdit.text()
        print(uid)
        value = self.firebase.validateUid(uid)
        print(value)
        if(value != None):
            self.buttonStart.setEnabled(True)
            self.buttonSaveUid.setEnabled(False)
        

    def ImageDifference(self,pastFrame,presentFrame):
        diff = cv2.absdiff(pastFrame,presentFrame)
        # print(diff.sum())
        return diff.sum()

    def motionCapture(self,img):
        
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        smoothed = cv2.filter2D(imgray,-1,WatcherUI.kernelSmooth)
        fgmask = WatcherUI.fgbg.apply(smoothed)

        dilation = cv2.dilate(fgmask,WatcherUI.kernel,iterations = 2)
        erosion = cv2.erode(dilation,WatcherUI.kernel,iterations = 5)

        ret,thresh = cv2.threshold(erosion,127,255,0)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        if self.ImageDifference(pastFrame=WatcherUI.pastFrame,presentFrame=WatcherUI.presentFrame) > WatcherUI.pixelDifference and WatcherUI.timeCheck !=  datetime.now().strftime('%Ss')  :
            timestampDay =  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")
            self.logCount += 1
            self.logsCount.display(self.logCount)
            self.listWidgetLogs.addItem(timestampDay)
            
            # cv2.imwrite( scriptDir + os.path.sep + timestampDay + '.jpg' , img) 
            retval, buffer = cv2.imencode('.jpg', img)
            jpg_as_text = base64.b64encode(buffer)
            self.firebase.saveImage(jpg_as_text)
            self.firebase.updateLog(timestampDay)
            self.firebase.sendNotification()
           
        WatcherUI.timeCheck = datetime.now().strftime('%Ss')    
        WatcherUI.pastFrame , WatcherUI.presentFrame  = WatcherUI.presentFrame , erosion



    def activate_watcher_button(self):
        print('Watcher Activated')
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)
        self.buttonStart.setEnabled(False)
        self.buttonStop.setEnabled(True)

    def update_frame(self):
        ret,self.image = self.cap.read()
        timeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestampDay =  datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")
        cv2.putText(self.image,timestampDay,(200,450), WatcherUI.font, 0.7,(255,100,100),2,cv2.LINE_AA)
        self.motionCapture(self.image)
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
        self.buttonStart.setEnabled(True)
        self.buttonSaveUid.setEnabled(True)
        self.buttonStop.setEnabled(False)

   

    def save_logs_button(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        i = 0
        logs = []
        for log in self.listWidgetLogs.item(i).text() :
            logs.append(log)
            i+=1 
        # print(logs)

        file = open(scriptDir + os.path.sep +'Watcherlogs.txt','a+')
        for log in logs:
            file.write(log +'\n') 
        file.close()
        print('Logs saved Sucessfully')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    watch = WatcherUI()
    watch.show()
    sys.exit(app.exec_())

