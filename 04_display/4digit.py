import RPi.GPIO as GPIO
import time

# GPIO 7개 핀 빈호 설정
#               A, B, C, D, E, F, G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]
DIGIT_PINS = [10, 11, 12, 13]

GPIO.setmode(GPIO.BCM)

for setment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.out)
    GPIO.output(segment, GPIO. LOW)

# Digit 핀은 HIGH->OFF, LOW->ON
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

def display(digit, number): # 자리수 , 숫자
    # 해당하는 자릿수의 핀만 LOW로 설정하고 나머지는 HIGH로 설정한다. 
    for i in range(4):  # 0~3
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

# 숫자출력
    for i in range(7): # 0~6
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.1) 


try:
    while True:
        display(1,2)
        display(2,0)
        display(3,2)
        display(4,1)

finally:
    GPIO.cleanup()
    print('Bye Bye')