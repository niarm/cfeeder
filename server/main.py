import RPi.GPIO as GPIO 
#from physicalmachine.steppercontroller import StepperController
from physicalmachine.servocontroller import ServoController
from time import sleep

class CatfeederMainApplication():
    def __init__(self):
        self.setup()
        try:
            while True:
                self.run()
        except KeyboardInterrupt:
            #print('An exception occurred: {}'.format(error))
            #GPIO.cleanup()
            print("cleanup GPIO not done")

    def setup(self):
        print("Starting Catfeeder Main Application");
        GPIO.setwarnings(False)
        #self.stepperLeft = StepperController(stepper_id=1, pin_enable=22, pin_step=27, pin_dir=17 )
        self.servo = ServoController(17)

    def run(self):
        #self.checkSensors()
        #steps = int(input("Steps?"))
        angle = float(input("Angle?"))
        self.servo.rotateTo(angle)
        #self.stepperLeft.rotateSteps(steps,1,delay)


    def checkSensors(self):
        a = 1

if __name__ == "__main__":
    app = CatfeederMainApplication()