import RPi.GPIO as GPIO
import time

LED1 = 4
LED2 = 5
LED3 = 6
GPIO.setmode(GPIO.BCM)      # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED1, GPIO.OUT)   # GPIO.OUT or GPIO.IN
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

GPIO.output(LED1, GPIO.HIGH) #1
print("Red led on")
time.sleep(2)
GPIO.output(LED1, GPIO.LOW)  #0
print("Red led off")
GPIO.output(LED2, GPIO.HIGH) #1
print("Yellow led on")
time.sleep(2)
GPIO.output(LED2, GPIO.LOW)  #0
print("Yellow led off")
GPIO.output(LED3, GPIO.HIGH) #1
print("Green led on")
time.sleep(2)
GPIO.output(LED3, GPIO.LOW)  #0
print("Green led off")
    

GPIO.cleanup()              # GPIO 핀상태 초기화