from lcd import drivers
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
DHT_PIN = 12 # 온도센서
GPIO.setmode(GPIO.BCM)
import datetime

display = drivers.Lcd()

try:
    print("Writing to display")
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        now=datetime.datetime.now()
        display.lcd_display_string('%.1f*, %.1f%%' % (t,h),2)
        display.lcd_display_string(now.strftime("%x%X"), 1)
        print(now.strftime("%x %X"))
        time.sleep(2)

finally:
    print("Cleaning up!")
    display.lcd_clear()
    GPIO.cleanup()