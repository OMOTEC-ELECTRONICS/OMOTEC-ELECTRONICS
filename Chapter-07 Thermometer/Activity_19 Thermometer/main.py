from machine import Pin
import onewire, ds18x20, time

# Define the GPIO pin connected to the sensor
sensor_pin = Pin(16)  # Change this to your GPIO pin

# Create the onewire object
ds_sensor = ds18x20.DS18X20(onewire.OneWire(sensor_pin))

# Scan for devices on the bus
roms = ds_sensor.scan()

while True:
    # Perform temperature conversion
    ds_sensor.convert_temp()

    # Wait for the conversion to finish
    time.sleep_ms(750)

    # Read the temperature from the sensor
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        print("Temperature:", temp, "Celsius")

    # Wait before taking the next reading
    time.sleep(1)
