from flask import Flask
from flask import render_template
from os import *
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

app=Flask(__name__)
@app.route("/")
def hello():
    return "gpiopi"
@app.route('/power/<pin_number>/<power_command>')
def power(pin_number,power_command):
    pin_number=int(pin_number)
    # show the user profile for that user
    if(power_command=='on'):
      GPIO.setup(pin_number, GPIO.OUT)
      GPIO.output(pin_number,GPIO.HIGH)
    if(power_command=='off'):
      GPIO.setup(pin_number,GPIO.OUT)
      GPIO.output(pin_number,GPIO.LOW)
    return '%s %s' % (pin_number,power_command)
@app.route('/power_on_1s/<pin_number>')
def power_on_1s(pin_number):
    pin_number=int(pin_number)
    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(pin_number,GPIO.LOW)
    return '%s ok' % (pin_number)
#device
@app.route('/device/<name>')
def device(name=None):
    return render_template('device.html', name=name)
