from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

WIDTH = 128
HEIGHT = 64
SCROLL_SPEED = 0.2  # Adjust the scrolling speed

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

scroll_text = "Smile, sip water, munch on good snacks, and enjoy playtime for a super-duper healthy you!"  # Enter your text here
text_width = len(scroll_text) * 8  # Each character is 8 pixels wide

while True:
    for i in range(text_width + WIDTH):  # Scroll through the entire text
        oled.fill(0)
        oled.text(scroll_text, int(WIDTH - i), 20)
        oled.show()