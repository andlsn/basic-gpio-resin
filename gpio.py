import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)

yellow = 7
red = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

GPIO.output(yellow, 0)
GPIO.output(red, 0)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/yellowON/", methods=['POST'])
def turnONYellowLED():

    print "Turn on yellow LED"
    GPIO.output(yellow, 1)

    return render_template('index.html');


@app.route("/yellowOFF/", methods=['POST'])
def turnOFFYellowLED():

    print "Turn off yellow LED"
    GPIO.output(yellow, 0)

    return render_template('index.html');


@app.route("/redON/", methods=['POST'])
def turnONRedLED():

    print "Turn on red LED"
    GPIO.output(red, 1)

    return render_template('index.html');


@app.route("/redOFF/", methods=['POST'])
def turnOFFRedLED():

    print "Turn off red LED"
    GPIO.output(red, 0)

    return render_template('index.html');

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
