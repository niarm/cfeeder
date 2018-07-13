import RPi.GPIO as GPIO 
from physicalmachine.steppercontroller import StepperController
from time import sleep

class CatfeederMainApplication():
    def __init__(self):
        self.setup()
        try:
            while True:
                self.run()
        except:
            GPIO.cleanup()
            print("cleanup GPIO done")

    def setup(self):
        print("Starting Catfeeder Main Application");
        self.stepperLeft = StepperController(stepper_id=1, pin_enable=22, pin_step=27, pin_dir=17 )

    def run(self):
        #self.checkSensors()
        #self.checkSensors()
        sleep(5.0)
        self.stepperLeft.rotateSteps(10,1)


    def checkSensors(self):
        a = 1

if __name__ == "__main__":
    app = CatfeederMainApplication()