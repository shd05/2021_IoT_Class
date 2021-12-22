# 도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 392) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 392) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 440) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 440) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 392) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 392) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 330) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음


pwm = GPIO.PWM(BUZZER_PIN, 392) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 392) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 330) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 330) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음

pwm = GPIO.PWM(BUZZER_PIN, 294) # 4옥타브 도음 (262 주파수)
pwm.start(10) #dutycycle (0~100) 소리크기

time.sleep(0.5)
pwm.ChangeDutyCycle(0) #부저음이 들리지 않음


pwm.stop()
GPIO.cleanup()
