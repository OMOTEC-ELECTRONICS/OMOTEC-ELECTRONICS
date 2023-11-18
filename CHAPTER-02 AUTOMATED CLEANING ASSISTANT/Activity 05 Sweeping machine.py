from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(16))
servoPin.freq(50)

def servo(degrees):
    # set max and min duty
    maxDuty = 9000
    minDuty = 1000
    # new duty is between min and max duty in proportion to its value
    newDuty = minDuty + (maxDuty - minDuty) * (degrees / 180)
    # servo PWM value is set
    servoPin.duty_u16(int(newDuty))

while True:
    # start increasing loop 0 to 180
    for degree in range(0, 180, 10):
        servo(degree)
        sleep(0.1)
        print("increasing -- " + str(degree))
    # start decreasing loop 180 to 0
    for degree in range(180, 0,-10):
        servo(degree)
        sleep(0.1)
        print("decreasing -- " + str(degree))
