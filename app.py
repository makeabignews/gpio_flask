from flask import Flask
from flask import render_template
from os import *
app=Flask(__name__)
@app.route("/")
def hello():
    return "gpiopi"
@app.route('/power/<pin_number>/<power_command>')
def power(pin_number,power_command):
    # show the user profile for that user
    if(power_command=='on'):
      system('sudo ./power.sh %s %s' % (pin_number,1))
    if(power_command=='off'):
      system('sudo ./power.sh %s %s' % (pin_number,0))
    return '%s %s' % (pin_number,power_command)
#device
@app.route('/device/<name>')
def device(name=None):
    return render_template('device.html', name=name)
