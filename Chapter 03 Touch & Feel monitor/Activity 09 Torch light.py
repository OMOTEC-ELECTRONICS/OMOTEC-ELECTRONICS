from machine import Pin, ADC
import time

# Create an ADC object linked to pin 26
adc = ADC(Pin(28, mode=Pin.IN))
led = Pin(15, Pin.OUT)

while True:
    # Read ADC and convert to voltage
    val = adc.read_u16()
    print(val)
    time.sleep_ms(1000)
    
    if val <= 60000:  # Compare val directly without calling it as a function
        led.value(1)
        time.sleep_ms(100)
    else:
        led.value(0)

    time.sleep_ms(100)
