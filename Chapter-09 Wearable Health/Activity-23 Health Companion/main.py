from imu import MPU6050
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import time

WIDTH = 120
HEIGHT = 32

i2c1 = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c1)

i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=200000)
imu = MPU6050(i2c)

buzzer_pin = Pin(17)
pwm = PWM(buzzer_pin)
pwm.freq(1000)

prev_gx = 0  # Variable to store the previous x-reading
shake_threshold = 15  # Adjust this threshold based on your sensitivity requirement
stable_threshold = 5  # Adjust this threshold based on your stability requirement

while True:
    gx = round(imu.gyro.x)
    gy = round(imu.gyro.y)
    gz = round(imu.gyro.z)

    print("X", gx, "\t", "Y", gy, "\t", "z", gz, "\t")

    # Calculate the change in acceleration
    acceleration_change = abs(gx - prev_gx)

    if acceleration_change > shake_threshold:
        oled.fill(0)
        oled.text("Check movement!", 0, 15)
        pwm.duty_u16(32767)
        time.sleep(2)  # Sleep for 2 seconds
    else:
        oled.fill(0)
        oled.text("Good", 0, 15)
        pwm.duty_u16(0)

    oled.show()

    prev_gx = gx  # Update previous x-reading
    time.sleep(1)

