from pyzbar.pyzbar import decode
import pyzbar.ImageScanner
from PIL import Image
import os 
import cv2

scriptDir = os.path.dirname(os.path.realpath(__file__))
qr  = scriptDir + os.path.sep + "horn.png"
print(decode(Image.open(qr)))


# cap = cv2.VideoCapture(0)

# while(1):
#     ret,frame = cap.read()
#     cv2.imshow("" , frame )
#     k = cv2.waitKey(30) & 0xff 
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

