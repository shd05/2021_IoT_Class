import RPi.GPIO as GPIO 
import time 

LED_PIN = 4
LED_PIN2 = 5
LED_PIN3 = 6

GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN , GPIO.OUT) # GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN2 , GPIO.OUT) # GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN3 , GPIO.OUT) # GPIO.OUT or GPIO.IN

GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(2)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.output(LED_PIN2, GPIO.HIGH)
time.sleep(2)       
GPIO.output(LED_PIN2, GPIO.LOW)

GPIO.output(LED_PIN3, GPIO.HIGH)
time.sleep(2)
GPIO.output(LED_PIN3, GPIO.LOW)

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("led on")
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("led off")
    time.sleep(1)
GPIO.cleanup()

