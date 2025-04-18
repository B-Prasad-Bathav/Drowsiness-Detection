import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

in1 = 17
in2 = 27
en_a = 4



GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)


q=GPIO.PWM(en_a,100)
q.start(50)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)

while(True):
   


         
   print("=== here ===")
# Wrap main content in a try block so we can  catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent the user seeing lots of unnecessary error messages.

