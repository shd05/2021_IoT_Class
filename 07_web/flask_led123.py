from flask import Flask
import RPi.GPIO as GPIO
LED_PIN = 12
LED_PIN2 = 4
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello_world():
    return'''
    
    <p>Hello, Flask!</p>
    <a href="/RED/led/on">RED LED ON</a>
    <a href="/RED/led/off">RED LED OFF</a>    
    <a href="/BLUE/led/on">BLUE LED ON</a>
    <a href="/BLUE/led/off">BLUE LED OFF</a>      
    ''' 

@app.route("/<cmd>/led/<op>")
def led_op(cmd,op):
    if op=="on":
        if cmd=="RED":
            GPIO.output(LED_PIN,GPIO.HIGH)
            return '''<p>RED LED ON</p>
            <a href="/">Go Home</a>  '''  
        elif cmd=="BLUE":
            GPIO.output(LED_PIN2,GPIO.HIGH)
            return '''<p>BLUE LED ON</p>
            <a href="/">Go Home</a>  '''

    elif op == "off":
        if cmd=="BLUE":
            GPIO.output(LED_PIN2,GPIO.LOW)
            return '''<p>BLUE LED OFF</p>
            <a href="/">Go Home</a>  '''

            
        elif cmd=="RED":
            GPIO.output(LED_PIN, GPIO.LOW)
            return '''<p>RED LED OFF</p>
            <a href="/">Go Home</a>  '''



if __name__ == "__main__":
    try:    
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()