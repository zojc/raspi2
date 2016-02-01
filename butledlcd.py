#!/usr/bin/python
import sys

sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD

lcd=Adafruit_CharLCD()     # instantiate LCD Display
lcd.clear()

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#GPIO_LED1 = 4
#GPIO_LED2 = 17
#GPIO.LED3 = 18
#GPIO.LED4 = 24
#GPIO_GUMB1 = 27
#GPIO_GUMB2 = 22
#GPIO_GUMB3 = 23
#GPIO_GUMB4 = 25

GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.output(4,0)
GPIO.output(17,0)
GPIO.output(18,0)
#GPIO.output(24,0)

try:
        while True:
                GPIO.output(4, GPIO.input(27) )
                GPIO.output(17, GPIO.input(22) )
                GPIO.output(18, GPIO.input(23) )
                #GPIO.output(24, GPIO.input(25) )
		if(GPIO.input(27) == 1):
			lcd.message('Ljubljana ima\n287.347 preb.')
			sleep(3)
			lcd.clear()
		if(GPIO.input(22) == 1):
			lcd.message('Celje ima 48.901\nprebivalcev')
                        sleep(3)
                        lcd.clear()
		if(GPIO.input(23) == 1):
                        lcd.message('Maribor ima\n111.735 preb.')
                        sleep(3)
                        lcd.clear()


except KeyboardInterrupt:
        GPIO.cleanup()

