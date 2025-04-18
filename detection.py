
import cv2

from picamera2 import Picamera2
from model import FacialExpressionModel
import numpy as np
import streamlit as st


# Grab images as numpy arrays and leave everything else to OpenCV.

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cv2.startWindowThread()
model = FacialExpressionModel("model.json", "model_weights.h5")

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

while True:
    im = picam2.capture_array()

    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    for (x, y, w, h) in faces:
        fc = grey[y:y+h, x:x+w]
		
        roi = cv2.resize(fc, (48, 48))
		
        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
        
        print('predected emotion == ', pred)

        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Camera", im)
    cv2.waitKey(1)
