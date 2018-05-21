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
# Fetch the service account key JSON file contents
cred = credentials.Certificate('H:/Github/PythonScripts/Firebase/AdminSdk.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythonfirebase-449e8.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/')
print (ref.get() )

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

db = firestore.client()
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})

users_ref = db.collection(u'users')
docs = users_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))