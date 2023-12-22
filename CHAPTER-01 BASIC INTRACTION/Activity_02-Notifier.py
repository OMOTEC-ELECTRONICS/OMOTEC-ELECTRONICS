import machine
import utime

# Define the button pin with a pull-up resistor
Button = machine.Pin(15, machine.Pin.PULL_DOWN)

while True:
    # Print the current state of the button (0: pressed, 1: not pressed)
    print(Button.value())
 # Check if the button is pressed
    if Button.value() == 1:
        # Print a message and wait for 0.5 second to avoid rapid triggering
        print("Patient Assistance Requested: Room 203")
        utime.sleep(0.5)
    else:
        # Print a placeholder message and wait for 0.5 second
        print("--")
        utime.sleep(0.5)
