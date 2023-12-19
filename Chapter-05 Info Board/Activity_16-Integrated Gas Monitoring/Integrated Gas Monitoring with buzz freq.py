from machine import ADC, Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
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

# OLED configuration
WIDTH = 120
HEIGHT = 32
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

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

    # Display sensor readings on OLED
    oled.fill(0)
    oled.text("Gas Values: {}".format(sensor_value), 0, 10)
    oled.text("Percentage: {:.2f}%".format(percentage), 0, 20)
    oled.show()

    # Wait for a short delay before the next reading (1 second in this case)
    utime.sleep(1)
