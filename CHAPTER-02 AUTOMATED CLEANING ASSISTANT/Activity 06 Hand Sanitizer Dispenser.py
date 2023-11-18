from machine import Pin, PWM
from time import sleep

# IR sensor configuration
IR = Pin(16, Pin.IN)

# Servo motor configuration
servoPin = PWM(Pin(17))
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
    # Check IR sensor
    if IR.value() == 0:
        print("Turning on Hand Sanitizer Dispenser")
        # Move the servo based on IR detection
        for degree in range(0, 180, 10):
            servo(degree)
            sleep(0.1)
        sleep(1)
        print("Turning off Hand Sanitizer Dispenser")
        for degree in range(180, 0, -10):
            servo(degree)
            sleep(0.1)
    else:
        print("Hand Sanitizer Dispenser Machine","\n")
    
        sleep(1)
