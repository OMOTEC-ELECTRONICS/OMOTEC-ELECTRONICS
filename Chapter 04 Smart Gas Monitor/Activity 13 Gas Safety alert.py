from machine import ADC, Pin, PWM
import utime

# Set up the analog-to-digital converter (ADC) for the gas sensor
adc = ADC(Pin(27))

# Set up the PWM for the buzzer
buzzer_pin = Pin(17)
pwm = PWM(buzzer_pin)

# Min and Max values for the gas sensor
min_sensor_value = 0
max_sensor_value = 65535

# Set the initial frequency for the buzzer
pwm.freq(1000)

# Threshold for triggering the gas alert (adjust as needed)
gas_alert_threshold = 25

# Main loop for continuous sensor readings and emergency notification sound
while True:
    # Read analog value from the gas sensor
    sensor_value = adc.read_u16()

    # Calculate percentage based on the sensor's min and max values
    percentage = ((sensor_value - min_sensor_value) / (max_sensor_value - min_sensor_value)) * 100

    # Print the current gas sensor value and calculated percentage
    print("Surrounding Gas Values:", sensor_value)
    print("Percentage:", percentage, "%")

    # Set the buzzer frequency based on the gas percentage
    buzzer_frequency = int(percentage * 10) + 1000
    pwm.freq(buzzer_frequency)

    # Check if gas concentration exceeds the threshold for an alert
    if percentage > gas_alert_threshold:
        # Trigger emergency notification sound
        # Increase duty cycle gradually, creating a rising pitch
        for duty in range(0, 65025, 1):
            pwm.duty_u16(duty)
            utime.sleep(0.0001)
        print("Gas concentration exceeds threshold! Take precautions.")
        # Decrease duty cycle gradually, creating a falling pitch
        for duty in range(65025, 0, -1):
            pwm.duty_u16(duty)
            utime.sleep(0.0001)

    # Pause between notifications
    utime.sleep(2)
