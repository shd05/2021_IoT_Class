import RPi.GPIO as GPIO
import time 

SWITCH_PIN = 8

GPIO.setmode(GPIO.BCM)
#내부풀업저항 설정 
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#풀 다운저항은 UP을 DOWN으로 바꾸면 됨

try:
        while True:
            val = GPIO.input(SWITCH_PIN)
            print(val)
            time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
