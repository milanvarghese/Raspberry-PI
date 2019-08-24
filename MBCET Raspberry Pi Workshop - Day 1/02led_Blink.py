#Importing Necessary Modules
import RPi.GPIO as GPIO
import time

#Raspberry pi terminal configuration
GPIO.setmode(GPIO.BOARD)

#Disabling all warning messages
GPIO.setwarnings(False)

#Assignming output pin numbers
led_pin=[3,5,7,11,13,15,19,21]

#Enabling the terminal pin on Raspberry
GPIO.setup(led_pin,GPIO.OUT)

#Function to make the bulb blink
while(1):
    for x in led_pin:
        GPIO.output(x,1)
        time.sleep(0.1)
    led_pin.reverse()
    for x in led_pin:
        GPIO.output(x,0)
        time.sleep(0.1)
    led_pin.reverse()