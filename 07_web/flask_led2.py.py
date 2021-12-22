from flask import Flask,render_template
import RPi.GPIO as GPIO
LED_PIN = 4
LED_PIN2 = 3
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello_world():
    return render_template("led.html")

@app.route("/<cmd>/led/<op>")
def led_op(cmd,op):
    if op=="on":
        if cmd=="RED":
            GPIO.output(LED_PIN,GPIO.HIGH)
            return '''LED ON  '''  
        elif cmd=="BLUE":
            GPIO.output(LED_PIN2,GPIO.HIGH)
            return '''LED ON '''

    elif op == "off":
        if cmd=="BLUE":
            GPIO.output(LED_PIN2,GPIO.LOW)
            return '''LED OFF '''

            
        elif cmd=="RED":
            GPIO.output(LED_PIN, GPIO.LOW)
            return '''LED OFF '''
    else:
        return'''URL Error''' 

if __name__ == "__main__":
    try:    
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.cleanup()