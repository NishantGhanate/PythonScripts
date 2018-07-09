from pyzbar.pyzbar import decode
from PIL import Image
import os 


scriptDir = os.path.dirname(os.path.realpath(__file__))

qr  = scriptDir + os.path.sep + "horn.png"
print(decode(Image.open(qr)))