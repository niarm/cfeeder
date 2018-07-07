from gpiozero import AngularServo
from gpiozero import Servo
from time import sleep

class ServoController:
    def __init__(self, pin, angle = 0):
        self.pin = pin
        self.angle = angle
        self.testMinMax()
    
    def setup(self):
        print("Setup ServoController for GPIO-Pin "+ str(self.pin))
        self.angularServo = AngularServo(pin=self.pin, initial_angle=self.angle)

    def testMinMax(self):
        print("Testing Servo Min/Max angle for GPIO-Pin "+ str(self.pin))
        self.servo = Servo(18)
        sleep(1.0)
        self.servo.min()
        sleep(2.0)
        self.servo.max()


    def rotateTo(self, angle):
        print("Rotating Servo at GPIO-Pin "+ self.pin +" to angle: "+ angle)
        self.angle = angle