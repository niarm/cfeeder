import RPi.GPIO as GPIO 
from time import sleep

class ServoController:
    def __init__(self, pin, angle = 0):
        self.pin = pin
        self.angle = angle
        self.setup()

    def setup(self):
        print("Setup ServoController for GPIO-Pin "+ str(self.pin))
        #self.angularServo = AngularServo(pin=self.pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(2.5)

    def rotateTo(self, desiredPosition):
        #self.angularServo.angle = desiredPosition
        #self.angle = desiredPosition
        self.dc = 1./18.*(desiredPosition)+2
        print("Rotating Servo at GPIO-Pin "+ str(self.pin) +"to pos: "+ str(desiredPosition) +" with dc: "+ str(self.dc))
        self.pwm.ChangeDutyCycle(self.dc)