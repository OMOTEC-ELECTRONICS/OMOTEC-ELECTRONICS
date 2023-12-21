from machine import Pin, ADC
import time

# Create an ADC object linked to pin 26
adc = ADC(Pin(26, mode=Pin.IN))

# Define input and output ranges
in_min, in_max = 0, 65535
out_min, out_max = 50, 90

while True:
    # Read ADC and convert to voltage
    val = adc.read_u16()
    
    # Map the ADC reading to a range of 1 to 100
    mapped_val = int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    print(mapped_val)
    time.sleep_ms(1000)
