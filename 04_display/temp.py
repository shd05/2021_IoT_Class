import RPi.GPIO as GPIO
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

PIN = 12 # 온도센서
PIR_PIN = 13 # PIR센서
LED_PIN2 = 5 # 빨간색 LED
LED_PIN3 = 7 # 초록색 LED
BUZZER_PIN = 11 # 피에조 부저
LED_PIN = 6 # 노란색 LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)
GPIO.setup(LED_PIN3,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)

time.sleep(1)
print('준비완료')
pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(40)
humidity = 0
temperature = 0
try:
    
    while True:
        val = GPIO.input(PIR_PIN) #PIR감지
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None: 
            GPIO.output(LED_PIN, GPIO.HIGH)# 노란색 LED작동
            print(humidity, temperature)  #온습도 정보 출력
            print('움직임 감지') # 움직임 감지 출력 

            if humidity>=80 and temperature>28: #습도가 80퍼센트 이상 온도가 28도 이상이면 피에조 부저와 빨간색 LED 작동

                    
                GPIO.output(LED_PIN2, GPIO.HIGH) #빨간색 LED작동
                print('불쾌') # 불쾌출력
                pwm.ChangeFrequency(292) # 도음출력
            
            elif humidity>=60 and temperature>=23:  #습도가 60퍼센트 이상 온도가 23도 이상이면 피에조 부저(레음)와  빨간색 LED 작동

                    
                GPIO.output(LED_PIN2, GPIO.HIGH) # 빨간색 LED작동
                print('보통') #'보통' 출력
                pwm.ChangeFrequency(330) # 피에조 부저 레음
            


            elif humidity<=60 and temperature<=23: #습도가 60퍼센트 이하 온도가 23도 이하이면  초록색 LED 작동후 쾌적표시
                GPIO.output(LED_PIN3, GPIO.HIGH)# 초록색 LED작동
                print('쾌적') #쾌적 출력
            

            else:
                print('움직임 없음') #움직임과 온습도 오류 출력
                GPIO.output(LED_PIN, GPIO.LOW) #노란색 LED 끄기
                print('온습도 오류')
            time.sleep(0.1)
            
 
finally:
    GPIO.cleanup()
    pwm.stop()
    print('cleanup and exit')

    
