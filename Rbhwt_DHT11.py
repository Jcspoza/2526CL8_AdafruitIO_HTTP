from machine import Pin
import time
import dht

# Initialize the DHT11 sensor
sensor = dht.DHT11(Pin(15))

while True:
   try:
      # Trigger measurement
      sensor.measure()
      # Read values
      temperature = sensor.temperature()  # In Celsius
      humidity = sensor.humidity()      # In Percent
      # Print values
      print(f"Temperature: {temperature:02d}°C   Humidity: {humidity:02d}%")
   except OSError as e:
      print("Failed to read sensor.")
   # Wait before the next reading
   time.sleep(2)
