import pigpio
from time import sleep

pi = pigpio.pi()

# loop forever

pi.set_servo_pulsewidth(12, 0)    # off
sleep(0.5)
pi.set_servo_pulsewidth(12, 2000) # position anti-clockwise
sleep(0.5)
pi.set_servo_pulsewidth(12, 0) # Off
sleep(1)



# pi.set_servo_pulsewidth(18, 1500) # position middle
# pi.set_servo_pulsewidth(18, 2000) # position clockwise

