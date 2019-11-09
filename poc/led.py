# Turn LED on/off GPIO 21 every 1 second
import RPi.GPIO as GPIO
import time

GPIO_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_PIN, GPIO.OUT)
try:
    while True:
	print "LED on"
	GPIO.output(GPIO_PIN, GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(GPIO_PIN, GPIO.LOW)
	time.sleep(1)
except KeyboardInterrupt:
    pass
