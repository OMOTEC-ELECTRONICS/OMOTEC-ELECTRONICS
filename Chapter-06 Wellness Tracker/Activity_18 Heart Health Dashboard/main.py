from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Initialize OLED
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Create an ADC object linked to pin 26
adc = ADC(Pin(26, mode=Pin.IN))

# Define input and output ranges for mapping
in_min, in_max = 0, 65535
out_min, out_max = 50, 65

while True:
    oled.fill(0)
    
    # Read ADC and convert to voltage
    val = adc.read_u16()
    
    # Map the ADC reading to a range of 50 to 90
    mapped_val = int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    # Display pulse sensor reading on OLED
    oled.text("Pulse Sensor:", 0, 20)
    oled.text(str(mapped_val), 0, 30)
    
    # Check if pulse rate is healthy (between 50 and 80)
    if 50 <= mapped_val <= 80:
        oled.text("Healthy!", 0, 50)
    else:
        oled.text("Not Healthy!", 0, 50)
    
    oled.show()
    
    time.sleep_ms(1000)
