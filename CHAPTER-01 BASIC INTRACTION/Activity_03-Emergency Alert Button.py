import machine
import utime

# Define GPIO pin numbers for Button, Buzzer, and LED
Button = machine.Pin(15, machine.Pin.IN)
buzzer = machine.Pin(17, machine.Pin.OUT)
led = machine.Pin(16, machine.Pin.OUT)

while True:
    # Check if the button is pressed
    if Button.value() == 1:
        # Alert message for an emergency
        print("Emergency in Ward A! Immediate response required.")

# Activate buzzer and LED for a brief duration
        buzzer.value(1)
        led.value(1)
        utime.sleep(0.5)

        # Deactivate buzzer after the alert
        buzzer.value(0)
        utime.sleep(0.5)
else:
        # No button press, print a placeholder message
        print("--")

        # Turn off LED and buzzer
        led.value(0)
        buzzer.value(0)

        # Pause briefly to avoid rapid polling
        utime.sleep(0.5)
