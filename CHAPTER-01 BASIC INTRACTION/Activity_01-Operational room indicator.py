from machine import Pin  
import utime            

# Initialize the LED pin
led = Pin(15, Pin.OUT)  
led.low()               

while True:
    	led.toggle()         
    	print("Toggle")     
    	utime.sleep(1)    