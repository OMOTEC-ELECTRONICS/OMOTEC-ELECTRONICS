from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import onewire, ds18x20, time

# OLED Setup
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Pulse Sensor Setup
adc = ADC(Pin(26, mode=Pin.IN))
in_min, in_max = 0, 65535
out_min, out_max = 50, 90

# DS18B20 Temperature Sensor Setup
sensor_pin = Pin(16)  # Change this to your GPIO pin
ds_sensor = ds18x20.DS18X20(onewire.OneWire(sensor_pin))
roms = ds_sensor.scan()

# RGB LED Setup
R_LED = Pin(18, Pin.OUT)
G_LED = Pin(19, Pin.OUT)
B_LED = Pin(20, Pin.OUT)


while True:
    # Pulse Sensor Reading
    oled.fill(0)
    val = adc.read_u16()
    mapped_val = int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    oled.text("Pulse Sensor:", 0, 20)
    oled.text(str(mapped_val), 0, 30)
    
    # Check pulse and set RGB LED color
    if 50 <= mapped_val <= 65:
        oled.text("Healthy!", 0, 50)
        G_LED.value(1)  # Green
    else:
        oled.text("Not Healthy!", 0, 50)
        R_LED.value(1)  # Red

    oled.show()
    time.sleep_ms(4000)  # Wait for 4 seconds

    # Temperature Reading
    ds_sensor.convert_temp()
    time.sleep_ms(750)

    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print("Temperature:", temp, "Celsius")

        # Check temperature and display caution
        oled.fill(0)
        oled.text("Temperature:", 0, 20)
        oled.text(str(temp), 0, 30)

        if temp > 30:  # Adjust the threshold as needed
            oled.text("Caution:High Temp!", 0, 50)
            R_LED.value(1)  # Red

        oled.show()
        time.sleep_ms(4000)  # Wait for 4 seconds
        R_LED.value(0)
        G_LED.value(0)
        B_LED.value(0)
        time.sleep_ms(4000)