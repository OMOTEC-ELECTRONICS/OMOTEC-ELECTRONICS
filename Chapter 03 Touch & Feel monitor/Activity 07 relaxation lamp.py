# Relaxation lamp

# Connect Red leg to GP26
# Connect Green leg to GP27
# Connect Blue leg to GP28

# NOTE - COMMON CATHODE LED USED

# Load libraries
import machine
import utime

# Configure outputs for each LED
R_LED = machine.Pin(26, machine.Pin.OUT)
G_LED = machine.Pin(27, machine.Pin.OUT)
B_LED = machine.Pin(28, machine.Pin.OUT)

print("Ready, Set, GO!")

while True:
    R_LED.value(0)  # Turn all Off
    G_LED.value(0)
    B_LED.value(0)
    utime.sleep(2)  # Pause time in second

    R_LED.value(1)  # Turn ON Red LED
    utime.sleep(2)  # Pause
    R_LED.value(0)  # Turn OFF Red LED
    B_LED.value(1)
    utime.sleep(2)  # Pause time in second
    B_LED.value(0)
    G_LED.value(1)
    utime.sleep(2)  # Pause time in second
    G_LED.value(0)
