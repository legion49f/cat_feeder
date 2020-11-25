import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    for dc in range(0, 100, 10):
        p.ChangeDutyCycle(dc)
        time.sleep(1)
    # for dc in range(100, -1, -5):
    #     p.ChangeDutyCycle(dc)
    #     time.sleep(0.2)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()