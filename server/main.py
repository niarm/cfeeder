from physicalmachine.servocontroller import ServoController
from time import sleep

class CatfeederMainApplication():
    def __init__(self):
        self.setup()
        while True:
            self.run()

    def setup(self):
        print("Starting Catfeeder Main Application");
        self.servoLeft = ServoController(pin=18)

    def run(self):
        #self.checkSensors()

        sleep(5.0)
        print("Rotate Servo To -90")
        self.servoLeft.rotateTo(0)
        sleep(5.0)
        print("Rotate Servo To 90")
        self.servoLeft.rotateTo(180)

    def checkSensors(self):
        a = 1

if __name__ == "__main__":
    app = CatfeederMainApplication()