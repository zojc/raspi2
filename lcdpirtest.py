import requests
import sys
import os
import urllib2
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
import RPi.GPIO as GPIO
from datetime import datetime

import Adafruit_DHT as dht

lcd=Adafruit_CharLCD()     # instantiate LCD Display
lcd.clear()

#from time import sleep, strftime
#import RPi.GPIO as GPIO
#from datetime import datetime

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up LED output
GPIO.setup(20, GPIO.OUT)

#Setup our API and delay
myAPI = "X31JTEKY3315SK0E"
myDelay = 15 #how many seconds between posting data

# Callback function to run when motion detected
def motionSensor(channel):
    GPIO.output(20, GPIO.LOW)
    if GPIO.input(21):     # True = Rising
        GPIO.output(20, GPIO.HIGH)

	
# add event listener on pin 21
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=200) 


print 'starting...'
	
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
print baseURL


try:
	while True:
		lcd.clear()
		lcd.message(datetime.now().strftime('%a %d.%m.%Y  \n%H:%M'))
      		sleep(10)
		
		h, t = dht.read_retry(dht.DHT22, 4)
		f = urllib2.urlopen(baseURL+"&field1=%s&field2=%s" % (h, t))
		lcd.clear()
		lcd.message("Temp.: {0:0.1f}".format(t))
		lcd.write4bits(223, True)
		lcd.message("C   \nVlaga: {0:0.1f}%".format(h))
		
		sleep(10)
    		
    		
finally:                   # run on exit
    	GPIO.cleanup()         # clean up
    	print "All cleaned up."	    		
	    	
