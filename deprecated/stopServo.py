# this is the file that runs to Feed the cats and gets executed from the Tkinter App or Web Gui
import RPi.GPIO as GPIO
import time

servoPIN1 = 16
servoPIN2 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


leftFeeder = GPIO.PWM(servoPIN1, 50) # GPIO 12 for PWM with 50Hz
leftFeeder.start(2.5) # Initialization
rightFeeder = GPIO.PWM(servoPIN2, 50) # GPIO 12 for PWM with 50Hz
rightFeeder.start(2.5)


leftFeeder.ChangeDutyCycle(0)
time.sleep(1)
rightFeeder.ChangeDutyCycle(0)
time.sleep(1)

leftFeeder

GPIO.cleanup()  
