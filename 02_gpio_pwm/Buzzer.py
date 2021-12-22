# 도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1) # 4옥타브 도음 (262 주파수)
pwm.start(100) #dutycycle (0~100) 소리크기

melody = [392,392,440,440,392,392,330,392,392,440,440,392,392,330]


try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(1)

finally:
    pwm.stop()
    GPIO.cleanup()
    