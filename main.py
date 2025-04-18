
import cv2
from scipy.spatial import distance
from imutils import face_utils
import dlib
from picamera2 import Picamera2
from model import FacialExpressionModel
import numpy as np
import RPi.GPIO as GPIO
import time
from gpiozero import LightSensor, LED, InputDevice

GPIO.setwarnings(False)

in1 = 17
in2 = 27
en_a = 4

sensor = InputDevice(23)
led = LED(16)
ldr = InputDevice(18)

# while True:
# 	ldr.wait_for_light()
# 	print("It's light! :)")
# 	ldr.wait_for_dark()
# 	print("It's dark :(")

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)



q=GPIO.PWM(en_a,100)
q.start(50)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)


# Grab images as numpy arrays and leave everything else to OpenCV.

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cv2.startWindowThread()
model = FacialExpressionModel("model.json", "model_weights.h5")

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear
	
thresh = 0.25
frame_check = 10
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]


picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

flag=0



while True:
	im = picam2.capture_array()

	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(grey, 1.1, 5)
 
	time.sleep(1)
	if(ldr.value == 1):
		led.on()
	else: 
		led.off()
		
	if(sensor.value == 0):
		q.ChangeDutyCycle(0)
		time.sleep(10)
	print("====== LDR Light ====== ", ldr.value)
	print("====== Sensor Dark  ====== ", sensor.value )

	subjects = detect(grey, 0)
    
	for (x, y, w, h) in faces:
		fc = grey[y:y+h, x:x+w]
		
		roi = cv2.resize(fc, (48, 48))
		
		pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
        
		#print('predected emotion == ', pred)
  
		if(pred == 'Angry'):
			q.ChangeDutyCycle(25)
			#time.sleep(5)
     
		elif(pred == 'Neutral'):
			q.ChangeDutyCycle(100)
			#time.sleep(5)

		cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

	for subject in subjects:
		shape = predict(grey, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(im, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(im, [rightEyeHull], -1, (0, 255, 0), 1)
		print("== ear == ", ear, " == thresh == ", thresh, " == condition == ", ear < thresh)
		if ear < thresh:
			flag += 1
			print (" FLAG == ",flag)
			if flag >= frame_check:
				cv2.putText(im, "****************ALERT!****************", (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(im, "****************ALERT!****************", (10,325),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				q.ChangeDutyCycle(0)
				print("==== Driver is sleeping === ")
				time.sleep(5)
				#print ("Drowsy")
		else:
			flag = 0
			
	cv2.imshow("Camera", im)
	cv2.waitKey(1)
	
