# 도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

melody = [392,392,440,440,392,392,330,392,392,440,440,392,392,330]

time.sleep(2)
#pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(1)

finally:
    pwm.stop()
    GPIO.cleanup()
    
