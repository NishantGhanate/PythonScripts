import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import storage as fb_storage

import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="H:/Github/FinalYearProject/Desktop/Config/Service.json"


class Firebase():
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('C:/Users/Nishant/Documents/AdminSdk.json')
        # As an admin, the app has access to read and write all data, regradless of Security Rules
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://smartsecurity-38229.firebaseio.com/',
        'storageBucket': 'gs://smartsecurity-38229.appspot.com'
    })
    print("")
       
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
        file = open('C:/Users/Nishant/Pictures/Spolier.png', 'rb')
        blob = file.read()
        file.close()
        doc_ref.set({"blob2":blob})

        # Then query for documents
        users_ref = db.collection(u'users')
        docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))    

firebase = Firebase()

firebase.PostImageFireStore()
