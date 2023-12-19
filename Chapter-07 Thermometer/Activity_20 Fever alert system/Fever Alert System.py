from machine import Pin, I2C, PWM
from onewire import OneWire
from ds18x20 import DS18X20
from ssd1306 import SSD1306_I2C
import utime

# Define the GPIO pin connected to the DS18B20 sensor
ds_sensor_pin = Pin(16)

# Create the onewire object
ds_sensor = DS18X20(OneWire(ds_sensor_pin))

# Scan for devices on the bus
roms = ds_sensor.scan()

# Set up the PWM for the buzzer
buzzer_pin = Pin(17)
pwm = PWM(buzzer_pin)

# Set up the initial frequency for the buzzer
pwm.freq(1000)

# Threshold for triggering the temperature alert (adjust as needed)
temperature_alert_threshold = 35

# OLED configuration
WIDTH = 120
HEIGHT = 32
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Main loop for continuous temperature readings and emergency notification sound
while True:
    # Perform temperature conversion for DS18B20 sensor
    ds_sensor.convert_temp()

    # Wait for the conversion to finish
    utime.sleep_ms(750)

    # Read the temperature from the DS18B20 sensor
    for rom in roms:
        temperature = ds_sensor.read_temp(rom)
        print("Temperature:", temperature, "Celsius")

        # Check if temperature exceeds the threshold for an alert
        if temperature > temperature_alert_threshold:
            # Trigger emergency notification sound
            pwm.duty_u16(32767)  # Set duty cycle to 50% for buzzing
            print("Temperature exceeds threshold! Take precautions.")
        else:
            # Turn off the buzzer if no alert
            pwm.duty_u16(0)

        # Display temperature on OLED
        oled.fill(0)
        oled.text("Temperature: {:.2f} C".format(temperature), 0, 10)
        oled.show()

    # Wait for a short delay before the next reading (1 second in this case)
    utime.sleep(1)
