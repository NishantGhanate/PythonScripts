import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import storage 
from firebase_admin import messaging
import datetime
import asyncio
import cv2
import numpy as np
import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Nishant/Documents/Service.json"
import base64

class Firebase():
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('C:/Users/Nishant/Documents/Service.json')
        # As an admin, the app has access to read and write all data, regradless of Security Rules
        self.registration_token = "cDoua1yH1ns:APA91bGURsSr_yM-JqsBntwpdE93Hoy_aTSwn_fjcYkBrUXHJHDM5P8fxVUr6AVGqpx1nn3tg-zV7QZDKRynrcKGdsTe-3IP9xxFitEwWdnehI66jTHdh6EX8qnjMfZ-69XKEVkXRESu"
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://smartsecurity-38229.firebaseio.com/',
        'storageBucket': 'gs://smartsecurity-38229.appspot.com'
    })
    
       
    def PostFireStore(self):
       # Add a new document
        db = firestore.Client()
        doc_ref = db.collection(u'users').document(u'Images')
        doc_ref.set({"blob":"blob"})

        # Then query for documents
        users_ref = db.collection(u'users')
        docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
        
    def PostImageFireStore(self):
       # Add a new document
        db = firestore.Client()
        doc_ref = db.collection(u'testing').document(u'Images')
        file = cv2.imread('C:/Users/Nishant/Pictures/Spolier.png')
        # blob = file.read()
        # file.close()
        doc_ref.set({"blob2":file})

        # Then query for documents
        users_ref = db.collection(u'users')
        docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))    

    def buck(self):
        bucket = storage.bucket()
        # image_data = open('C:/Users/Nishant/Pictures/Spolier.png','rb')
        with open("C:/Users/Nishant/Pictures/Spolier.png", "rb") as image:
            f = image.read()
            b = bytearray(f)
            print (b[0])
            
        blob = bucket.blob('new_cool_image.jpg')
        blob.upload_from_string(
                b,
                content_type='image/jpg'
            )
        print(blob.public_url)
        db = firestore.Client()
        doc_ref = db.collection(u'testing').document(u'Images')
        doc_ref.set({"blob2":b})
     
     
    def sentUnit(self):
        file = cv2.imread('C:/Users/Nishant/Pictures/Spolier.png')
        print( type(file) )
    
        with open("C:/Users/Nishant/Pictures/Spolier.png", "rb") as image:
            f = image.read()
            # print(type(f))
            # print(f)
            b = bytearray(f)
            print(b)
            print(type(b))
            s = str(b)
        
        img = cv2.imread('C:/Users/Nishant/Pictures/Geno.jpg')    
        retval, buffer = cv2.imencode('.jpg', img)
        jpg_as_text = base64.b64encode(buffer)
        
        a = open('C:/Users/Nishant/Pictures/B.txt','a+')
        a.write(str(jpg_as_text))
        a.close()
        
        # db = firestore.Client()
        # doc_ref = db.collection(u'testing').document(u'Images')
        # doc_ref.set({"blob3":jpg_as_text})
    
    async def sendNotificatin(self):

        # See documentation on defining a message payload.
        message = messaging.Message(
            data={
                'title': '850',
                'body': '2:45',
            },
            token=self.registration_token,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send_all(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
    
        
    async def sendAll(self):
        # [START send_all]
        # Create a list containing up to 100 messages.
        messages = [
            messaging.Message(
                notification=messaging.Notification('Smart App', 'Alert !!!!!'),
                token=self.registration_token,
            ),
            # ...
            messaging.Message(
                notification=messaging.Notification('Price drop', '2% off all books'),
                topic='readers-club',
            ),
        ]

        response = messaging.send_all(messages)
        # See the BatchResponse reference documentation
        # for the contents of response.
        print('{0} messages were sent successfully'.format(response.success_count))
    
    async def android_message(self):
        # [START android_message]
        registration_token = "cDoua1yH1ns:APA91bGURsSr_yM-JqsBntwpdE93Hoy_aTSwn_fjcYkBrUXHJHDM5P8fxVUr6AVGqpx1nn3tg-zV7QZDKRynrcKGdsTe-3IP9xxFitEwWdnehI66jTHdh6EX8qnjMfZ-69XKEVkXRESu"
        message = messaging.Message(
            android=messaging.AndroidConfig(
                ttl=datetime.timedelta(seconds=3600),
                priority='normal',
                notification=messaging.AndroidNotification(
                    title='$GOOG up 1.43 on the day',
                    body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                    icon='stock_ticker_update',
                    color='#f45342'
                ),
            ),
            topic='industry-tech',
            token=self.registration_token
        )
        # [END android_message]
        print("Android ".format(message))
        
    async def send_dry_run(self):
        message = messaging.Message(
            data={
                'score': '850',
                'time': '2:45',
            },
            token=self.registration_token,
        )

        # [START send_dry_run]
        # Send a message in the dry run mode.
        response = messaging.send(message, dry_run=True)
        # Response is a message ID string.
        print('Dry run successful:', response)
        # [END send_dry_run]  
    async def all_platforms_message(self):
    # [START multi_platforms_message]
        message = messaging.Message(
            notification=messaging.Notification(
                title='$GOOG up 1.43% on the day',
                body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
            ),
            android=messaging.AndroidConfig(
                ttl=datetime.timedelta(seconds=3600),
                priority='normal',
                notification=messaging.AndroidNotification(
                    icon='stock_ticker_update',
                    color='#f45342'
                ),
            ),
            apns=messaging.APNSConfig(
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(badge=42),
                ),
            ),
            topic='industry-tech',
        )
        # [END multi_platforms_message]
        return message
      
firebase = Firebase()

loop = asyncio.get_event_loop()
task1 = loop.create_task(firebase.sendNotificatin())
task2 =  loop.create_task(firebase.sendAll())
task3 = loop.create_task(firebase.send_dry_run())
task4 = loop.create_task(firebase.all_platforms_message())
loop.run_until_complete(asyncio.gather(task1,task2,task3,task4))
