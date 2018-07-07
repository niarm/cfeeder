from physicalmachine.servocontroller import ServoController

class CatfeederMainApplication():
    def __init__(self):
        self.setup()
        while True:
            self.run()

    def setup(self):
        print("Starting Catfeeder Main Application");
        self.servoLeft = ServoController(pin=17)

    def run(self):
        self.checkSensors()

    def checkSensors(self):
        a = 1

if __name__ == "__main__":
    app = CatfeederMainApplication()