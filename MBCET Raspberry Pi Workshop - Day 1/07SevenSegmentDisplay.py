#Importing Necessary Modules
import RPi.GPIO as GPIO
import time

#Raspberry pi terminal configuration
GPIO.setmode(GPIO.BOARD)

#Disabling all warning messages
GPIO.setwarnings(False)

#Assignming output pin numbers
pin=[3,5,7,11,13,15,19,21]
#Defining a Two dimensional list to display each numbers
num=[[5,7,11,13,15,19],[11,19],[7,11,3,13,15],[7,11,3,19,15],[5,3,11,19],[7,5,3,19,15],[7,5,3,13,15,19],[7,11,19],[3,5,7,11,13,15,19],[3,5,7,11,19]]

#Enabling the terminal pin on Raspberry
GPIO.setup(led_pin,GPIO.OUT)


#Building a function to initialize the device with all light off
def off():
    for x in pin:
        led.output(x,0)

#Function to Make the device display a number for the curresponding input number
ind=0
while True:
    ind=int(input("Enter an number between 0-9: "))
    off()
    for y in range(len(num[ind])):
        led.output(num[ind][y],1)