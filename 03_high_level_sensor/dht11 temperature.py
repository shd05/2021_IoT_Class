import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 12

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if humidity is not None and temperature is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' % (temperature, humidity))
        else:
            print('Read Error')
               

finally:
     print("Bye Bye")
        
