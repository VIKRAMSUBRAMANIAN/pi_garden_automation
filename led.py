import RPi.GPIO as GPIO
import time
from trial  import generate_value
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "done"
 generate_value() == 1:
    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")

 else:
       print("Nope")

GPIO.output(18,GPIO.LOW)

