#Importing Necessary Modules
import RPi.GPIO as GPIO
import time

#Raspberry pi terminal configuration
GPIO.setmode(GPIO.BOARD)

#Disabling all warning messages
GPIO.setwarnings(False)

#Assignming output pin numbers
led_pin=[3,5,7]

#Enabling the terminal pin on Raspberry
GPIO.setup(led_pin,GPIO.OUT)

#Function to make led blink different colours one after other
while(1):
    for x in led_pin:
        led.output(x,1)
        time.sleep(2)
    for x in led_pin:
        led.output(x,0)
        time.sleep(2)