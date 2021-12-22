from lcd import drivers
import time

display = drivers.Lcd()
humidity = 0
temperature = 0
try:
    print("Writing to display")
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        display.lcd_display_string("Hello, World!!", 1)
        display.lcd_display_string("** WELCOME **", 2)
        time.sleep(2)
        display.lcd_display_string("Hello, World!!", 1)
        display.lcd_display_string("  WELCOME  ", 2)
        time.sleep(2)
finally:
    print("Cleaning up!")
    display.lcd_clear()