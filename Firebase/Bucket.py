from firebase_admin import storage 
from firebase_admin import credentials
import firebase_admin
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="H:/Github/PythonScripts/Firebase/AdminSdk.json"

cred = credentials.Certificate('H:/Github/PythonScripts/Firebase/AdminSdk.json')
        # As an admin, the app has access to read and write all data, regradless of Security Rules
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://pythonfirebase-449e8.firebaseio.com',
        'storageBucket': 'gs://pythonfirebase-449e8.appspot.com'
    })

# firebase = firebase.FirebaseApplication('https://pythonfirebase-449e8.firebaseio.com')


bucket = storage.bucket()
# posting to firebase storage
print(bucket)

imageBlob = bucket.blob("/")
# imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
imagePath = 'science.jpg'
imageBlob = bucket.blob(os.path.basename('‪D:/logo/science.jpg'))
print (imageBlob)
bucket
imageBlob.upload_from_filename(imagePath)