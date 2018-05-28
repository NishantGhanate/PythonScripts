# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 01:51:14 2018
python IDLE
@author: Nishant
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import storage as fb_storage

from google.cloud import storage
from google.oauth2 import service_account
from PIL import Image
import simplejson as json


class Firebase:
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('H:/Github/PythonScripts/Firebase/AdminSdk.json')
        # As an admin, the app has access to read and write all data, regradless of Security Rules
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://pythonfirebase-449e8.firebaseio.com',
        'storageBucket': 'gs://pythonfirebase-449e8.appspot.com'
    })
  

    def PostFireStore(self):
        self.FirestoreDb = firestore.client()
        doc_ref = self.FirestoreDb.collection(u'users').document(u'alovelace')
        doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })

    def GetFireStore(self):
        users_ref = self.FirestoreDb.collection(u'users')
        docs = users_ref.get()
        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))

    def PostFirebase(self):
        ref = db.reference('/')
        users_ref = ref.child('users')
        users_ref.set({
        'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
        },
        'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
        }
    })

    def GetFireBase(self):
        ref = db.reference('/')
        print (ref.get() )


    def PostImage(self):
        # bucket = fb_storage.bucket()
        
        # print(client)

        with open('H:/Github/PythonScripts/Firebase/AdminSdk.json') as source:
            info = json.load(source)
        storage_credentials = service_account.Credentials.from_service_account_info(info)
        print( storage_credentials)
        client = storage.Client()
        print(client)
        # bucket = client.get_bucket()
        # print(bucket)
        # blob = bucket.blob('H:/Github/OpenCv/Research/images/heart.jpg')
     
    
        # of = open('H:/Github/OpenCv/Research/images/heart.jpg', 'rb')
        # blob.upload_from_file(of)
        # or... (no need to use pillow if you're not transforming)
        #blob.upload_from_filename(filename=outfile)

firebase = Firebase()

firebase.PostImage()




