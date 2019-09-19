import cv2
import base64
import numpy as np

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def get_frame(self):
        ret, img = self.cap.read()
        return (cv2.imencode('.jpg', img)[1].tostring())
        