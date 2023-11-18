import machine
import utime
IR = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(17, machine.Pin.OUT)
while True:
    if IR.value() == 0:
        led.value(1)
        print("IR Sensor Detected!")
        utime.sleep(1)
    else:
        led.value(0)
        print("NOT Detected!")
        utime.sleep(1)
        
        
        