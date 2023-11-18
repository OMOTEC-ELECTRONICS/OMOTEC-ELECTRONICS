from machine import ADC, Pin
import utime

# Set up the analog-to-digital converter (ADC)
adc = ADC(Pin(27))  

# Min and Max values for the sensor
min_sensor_value = 0
max_sensor_value = 65535

# Main loop for continuous sensor readings
while True:
    # Read analog value from the sensor
    sensor_value = adc.read_u16()

    # Calculate percentage based on the sensor's min and max values
    percentage = ((sensor_value - min_sensor_value) / (max_sensor_value - min_sensor_value)) * 100

    # Print the current sensor value and calculated percentage
    print("Surronding Gas Values:", sensor_value)
    print("Percentage:", percentage,"%")

    # Wait for a short delay before the next reading (1 second in this case)
    utime.sleep(1)
