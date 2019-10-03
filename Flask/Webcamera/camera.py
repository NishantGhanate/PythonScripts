import cv2
import base64
import numpy as np

class Camera:
    black = np.zeros(shape=[480, 640], dtype=np.uint8)
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def get_frame(self):
        ret, img = self.cap.read()
        if ret:
            return (cv2.imencode('.jpg', img)[1].tostring())
        return (cv2.imencode('.jpg', black)[1].tostring())
        
        