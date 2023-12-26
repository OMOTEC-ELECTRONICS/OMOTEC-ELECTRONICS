from imu import MPU6050
import time
from machine import Pin, I2C

led = Pin(15, Pin.OUT)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)
counter = 0  # Initialize the counter variable

while True:
    print("Gyrometer value")
    gx = round(imu.gyro.x)

    print("X", gx)
    
    if gx <= 1:
        led.value(1)
        counter += 1  # Increment the counter
        print("steps:", counter)
    else:
        led.value(0)
    time.sleep(1)