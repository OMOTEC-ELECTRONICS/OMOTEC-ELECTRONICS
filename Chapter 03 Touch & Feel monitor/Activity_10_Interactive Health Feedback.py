from machine import Pin, ADC
import time
import utime

# Create an ADC object linked to pin 28
adc = ADC(Pin(28, mode=Pin.IN))

# Configure outputs for each LED
R_LED = Pin(26, Pin.OUT)
G_LED = Pin(27, Pin.OUT)
B_LED = Pin(16, Pin.OUT)

print("Ready, Set, GO!")

while True:
    # Read ADC and convert to voltage
    val = adc.read_u16()
    print(val)
    time.sleep_ms(1000)
    
    if val <= 60000:
        R_LED.value(0)
        G_LED.value(1)
        B_LED.value(0)
        time.sleep_ms(2)
    else:
        R_LED.value(1)
        G_LED.value(0)
        B_LED.value(0)
        time.sleep_ms(2)