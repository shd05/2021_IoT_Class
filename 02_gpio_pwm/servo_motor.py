# servo_motor.py
import RPi.GPIO as GPIO


SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# 주파수 설정(50hZ)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm. start(7.5) #Duty cycle

try:
    while True:
        val= input('1: -90, 2: 0, 3: +90 9: exit>') #1번 누르면 -90
        if val =='1':
            pwm.ChangeDutyCycle(2.5) #-90도 (5)-> -45도
        elif val == '2':
            pwm.ChangeDutyCycle(7.5)
        elif val =='3':
            pwm.ChangeDutyCycle(12.5) #+90도 (10)-> + 45도
        elif val =='9':
            break
finally:
    pwm.stop()
    GPIO.cleanup()

