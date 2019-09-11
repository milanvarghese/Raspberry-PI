#Importing Necessary Modules
import RPi.GPIO as GPIO
import time

#Raspberry pi terminal configuration
GPIO.setmode(GPIO.BOARD)

#Disabling all warning messages
GPIO.setwarnings(False)

#Assignming output pin number
led_pin=3

#Enabling the terminal pin on Raspberry
GPIO.setup(led_pin,GPIO.OUT)

#Function to turn on the bulb
while(1):
    GPIO.output(led_pin,1)