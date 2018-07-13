from time import sleep
import RPi.GPIO as GPIO

class StepperController:
    def __init__(self, stepper_id, pin_enable, pin_step, pin_dir, steps_per_revolution=200):
        self.id = stepper_id
        self.pin_enable = pin_enable
        self.pin_step = pin_step
        self.pin_dir = pin_dir
        self.steps_per_revolution = steps_per_revolution
        self.delay = .02
        
        self.setup()

    def setup(self):
        print("setting up StepperController with GPIO-CONFIG: (EN = "+ str(self.pin_enable)+", STEP = "+ str(self.pin_step)+", DIR = "+ str(self.pin_dir) + ")")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_enable, GPIO.OUT)
        GPIO.setup(self.pin_step, GPIO.OUT)
        GPIO.setup(self.pin_dir, GPIO.OUT)

        GPIO.output(self.pin_enable, GPIO.LOW) #high is stop
        print("... setup done")

    def rotateSteps(self, num_steps, direction=1):
        print("Moving Stepper"+ str(self.id) +" for num_steps: "+ str(num_steps) + " in directon: "+str(direction)+"(CW=1, CCW=0)")
        GPIO.output(self.pin_dir, direction)
        
        for x in range(num_steps):
            GPIO.output(self.pin_step, GPIO.HIGH)
            sleep(self.delay)
            GPIO.output(self.pin_step, GPIO.LOW)
            sleep(self.delay)