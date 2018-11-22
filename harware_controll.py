import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
def turned_on():
    print "valve open"
    GPIO.output(18,GPIO.HIGH)
def turned_off():
    print "valve closed"
    GPIO.output(18,GPIO.LOW)
