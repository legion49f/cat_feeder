from gpiozero import Servo
import time

PINS = [12, 18]

for pin in PINS:
    servo = Servo(pin)
    servo.mid()
    time.sleep(1)