import machine
import utime

# Define the button pin with a pull-up resistor
Button = machine.Pin(15, machine.Pin.PULL_DOWN)

while True:
    # Print the current state of the button (0: pressed, 1: not pressed)
    print(Button.value())
 # Check if the button is pressed
    if Button.value() == 0:
        # Print a message and wait for 1 second to avoid rapid triggering
        print("Patient Assistance Requested: Room 203")
        utime.sleep(1)
    else:
        # Print a placeholder message and wait for 1 second
        print("--")
        utime.sleep(1)
