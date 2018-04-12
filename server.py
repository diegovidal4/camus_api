from flask import Flask
import RPi.GPIO as GPIO
import json

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

app = Flask(__name__)

@app.route('/relay/<any(1,0):action>', methods = ['GET'])
def move_relay(action):
    if action == 1:
        GPIO.output(22, GPIO.HIGH)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    else:
        GPIO.output(22, GPIO.LOW)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
