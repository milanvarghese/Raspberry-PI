#Importing Necessary Modules
import RPi.GPIO as GPIO

#Raspberry pi terminal configuration
GPIO.setmode(GPIO.BOARD)

#Disabling all warning messages
GPIO.setwarnings(False)

#Assignming output pin number and initial Pulse Width Modulation(PWM) value
led=[3,5,7]
pwm[]=[0,0,0]

#Enabling the terminal pin on Raspberry and setting inital PWM values
for x in led:
    GPIO.setup(x,GPIO.OUT)
    pwm[x]=GPIO.PWM(x,100)

#Notice on how to exit the program loop
print("\nPress Ctl C to quit\n")

#Function to automatically change the brightness of multiple leds with 5 units duty change
pwm.start(dc)
while True:
    dc=0
    for x in pwm:
        for dc in range(0,101,5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(.01)
            print(dc)
        for dc in range(95,0,-5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(.01)
        print(dc)