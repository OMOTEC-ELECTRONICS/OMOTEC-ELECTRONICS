import machine
import utime

# Configure outputs for each LED
Button1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
Button2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
R_LED = machine.Pin(26, machine.Pin.OUT)  # Red LED pin
G_LED = machine.Pin(27, machine.Pin.OUT)  # Green LED pin
B_LED = machine.Pin(28, machine.Pin.OUT)  # Blue LED pin
print("Ready, Set, GO!")

while True:
    if Button1.value() == 0:  # Assuming the button is active-low
        R_LED.value(0)  # Turn OFF RED LED
        B_LED.value(1)  # Turn ON BLUE LED
        G_LED.value(0)  # Turn OFF GREEN LED

    else:
        R_LED.value(0)  # Turn OFF RED LED
        G_LED.value(0)  # Turn OFF GREEN LED
        B_LED.value(0)	# Turn OFF BLUE LED
        
    if Button2.value() == 0:  # Assuming the button is active-low
        R_LED.value(0)  # Turn OFF RED LED
        B_LED.value(0)  # Turn OFF BLUE LED
        G_LED.value(1)  # Turn ON GREEN LED

    else:
        R_LED.value(0)  # Turn OFF RED LED
        G_LED.value(0)  # Turn OFF GREEN LED
        B_LED.value(0)	# Turn OFF BLUE LED