import pyqrcode

import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))

url = pyqrcode.create('http://uca.edu')
url.svg(scriptDir + os.path.sep +'uca-url.svg', scale=8)
url.eps(scriptDir + os.path.sep +'uca-url.esp', scale=2)

qr = pyqrcode.create("Welcome to Python World")
qr.png(scriptDir + os.path.sep + "horn.png", scale=6)


