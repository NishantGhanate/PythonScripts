# http://testphp.vulnweb.com/secured/newuser.php

# uuname: esds
# upass: 1
# upass2: 1
# urname: 
# ucc: sdsdsd
# uemail: sdsdsd
# uphone: dsdsdsd
# uaddress: 121212
# signup: signup


import requests
import string
import random

postUrl = "http://testphp.vulnweb.com/secured/newuser.php"

for _ in range(3):
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    phoneNumber = ''.join(random.choice(string.digits) for _ in range(10))
    formData = {
        'uuname' : username,
        'upass' : username ,
        'upass2' : username + '@gmail.com',
        'urname' : username,
        'ucc' : username,
        'uemail' : username,
        'uphone' : phoneNumber,
        'uaddress': 'dos',
        'signup' : 'signup'
    }
    print(formData)
    r = requests.post(postUrl, allow_redirects=False , data = formData)
    print(r)