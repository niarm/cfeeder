from gpiozero import AngularServo
from time import sleep

class ServoController:
    def __init__(self, pin, angle = 0):
        self.pin = pin
        self.angle = angle
        self.setup()

    def setup(self):
        print("Setup ServoController for GPIO-Pin "+ str(self.pin))
        self.angularServo = AngularServo(pin=self.pin)


    def rotateTo(self, angle):
        print("Rotating Servo at GPIO-Pin "+ str(self.pin) +" to angle: "+ str(angle))
        self.angularServo.angle = angle
        self.angle = angle