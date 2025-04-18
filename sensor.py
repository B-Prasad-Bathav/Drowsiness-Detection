from gpiozero import LightSensor, LED, InputDevice
from signal import pause

sensor = InputDevice(23)
led = LED(16)

ldr = InputDevice(18)

#sensor.when_dark = led.on
#sensor.when_light = led.off
led.on()
while(True):
	print("Sensor Value - ", sensor.value)
	print("LDR Value", ldr.value)


