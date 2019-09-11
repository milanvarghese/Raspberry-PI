#Importing Modules
import RPi.GPIO as sw
import time
#Initializing the board
sw.setmode(sw.BOARD)
sw.setwarnings(False)

#Assigning BOARD PINs and setting up the button and pins
sw_pin=5
led_pin=7
sw.setup(sw_pin,sw.IN,pull_up_down=sw.PUD_UP)
sw.setup(led_pin,sw.OUT)
sw.output(led_pin,0)

#Function to make the button work
while(1):
    x=sw.input(sw_pin)
    if x==0:
        while(1):
           sw.output(led_pin,1)
           time.sleep(.05)
           sw.output(led_pin,0)
           time.sleep(.05)
           x=sw.input(sw_pin)
           if x==1:
               break;
    else:
        sw.output(led_pin,0)