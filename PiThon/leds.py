import RPi.GPIO as GPIO
from time import sleep

red = 18
green = 23
blue = 24
button = 22
channels = (red, green, blue)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(button, GPIO.IN)


while True:
    if GPIO.input(button):
        GPIO.output(red, GPIO.HIGH)
        sleep(1)
        GPIO.output(red, GPIO.LOW)
        
        GPIO.output(green, GPIO.HIGH)
        sleep(1)
        GPIO.output(green, GPIO.LOW)
        
        GPIO.output(blue, GPIO.HIGH)
        sleep(1)
        GPIO.output(blue, GPIO.LOW)
        
    else:
        GPIO.output(channels, GPIO.LOW)
