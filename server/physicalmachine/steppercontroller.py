from time import sleep

class StepperController:
    def __init__(self, stepper_id, pin_enable, pin_step, pin_dir):
        self.id = stepper_id
        self.pin_enable = pin_enable
        self.pin_step = pin_step
        self.pin_dir = pin_dir
        
        self.setup()

    def setup(self):
        print("Setup StepperController for EN: "+ str(self.pin_enable)+"/ STEP: "+ str(self.pin_step)+"/ DIR: "+ str(self.pin_dir))

    def rotateSteps(self, num_steps):
        print("Moving Stepper"+ str(self.id) +" for num_steps: "+ str(num_steps))