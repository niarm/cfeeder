from time import sleep
from physicalmachine.steppermotor import stepper

class StepperController:
    def __init__(self, stepper_id, pin_enable, pin_step, pin_dir, steps_per_revolution=200):
        self.id = stepper_id
        self.pin_enable = pin_enable
        self.pin_step = pin_step
        self.pin_dir = pin_dir
        
        self.setup()

    def setup(self):
        print("setting up StepperController with GPIO-CONFIG: (EN = "+ str(self.pin_enable)+", STEP = "+ str(self.pin_step)+", DIR = "+ str(self.pin_dir) + ")")
        self.stepperMotor = stepper([self.pin_step, self.pin_dir, self.pin_enable])
        print("... setup done")

    def rotateSteps(self, num_steps, direction="right"):
        print("Moving Stepper"+ str(self.id) +" for num_steps: "+ str(num_steps) + " in directon: "+str(direction)+"(CW=1, CCW=0)")
        self.stepperMotor.step(num_steps, direction)