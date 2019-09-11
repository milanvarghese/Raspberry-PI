#Importing Necessary Modules
import RPi.GPIO as GPIO

#Raspberry pi terminal configuration
GPIO.setmode(GPIO.BOARD)

#Disabling all warning messages
GPIO.setwarnings(False)

#Assignming output pin number
led_pin=5

#Enabling the terminal pin on Raspberry
GPIO.setup(led_pin,GPIO.OUT)

#Function to light the led at a particular input brightness
pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(0)
while True:
    duty=int(input("Enter Brightness (0to 100): "))
    pwm_led.ChangeDutyCycle(duty)