import requests
import string
import random
from lxml import html
import time

postUrl = "http://127.0.0.1:8000/register"


for _ in range(2):
    page = requests.get(postUrl)
    tree = html.fromstring(page.content)
    token = tree.xpath('//input[@name = "_token"]/@value')
    print(token)

    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    formData = {
        '_token' : token,
        'name' : username ,
        'email' : username + '@gmail.com',
        'password' : username,
        'password_confirmation' : username
    }
    print(formData)
    r= requests.post(postUrl, allow_redirects=False , data = formData)
    print(r)
    time.sleep(5)



# username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
# print(username)
# page = requests.get(postUrl)
# tree = html.fromstring(page.content)
# tree = tree.xpath('//input[@name = "_token"]/@value')
# print(tree)
# <meta name="csrf-token" content="B9A4QQICIGZVzJ1Ay2sqTOlNa2McFgezG31dUFWT">     
#<form class="form-horizontal" method="POST" action="http://127.0.0.1:8000/register"><input type="hidden" name="_token" value="P4JaIeqSmxO821sVlFQKWTKwtWsTvicio7UCNAWT"> 
