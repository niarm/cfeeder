from gpiozero import AngularServo
from gpiozero import Servo
from time import sleep

class ServoController:
    def __init__(self, pin, angle = 0):
        self.pin = pin
        self.angle = angle
        self.setup()

    def setup(self):
        print("Setup ServoController for GPIO-Pin "+ str(self.pin))
        self.angularServo = AngularServo(pin=self.pin, initial_angle=self.angle, min_angle=-180, max_angle=180)


    def rotateTo(self, angle):
        print("Rotating Servo at GPIO-Pin "+ self.pin +" to angle: "+ angle)
        self.angularServo.angle = angle
        self.angle = angle