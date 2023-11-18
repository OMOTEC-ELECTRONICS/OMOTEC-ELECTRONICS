from machine import Pin, PWM
from time import sleep

# Define the GPIO pin for the buzzer
buzzer_pin = Pin(17)
pwm = PWM(buzzer_pin)

# Set the initial frequency
pwm.freq(1000)
 
# Main loop
while True:
    # Trigger emergency notification sound
    
    # Function to generate an emergency notification sound
    # Increase duty cycle gradually, creating a rising pitch
    for duty in range(0, 65025, 1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    
    # Decrease duty cycle gradually, creating a falling pitch
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    
    # Pause between notifications
    sleep(2)
