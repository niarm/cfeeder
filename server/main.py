from physicalmachine.servocontroller import ServoController

class CatfeederMainApplication():
    def __init__(self):
        self.run()

    def run(self):
        print("Starting Catfeeder Main Application");
        self.servoLeft = ServoController(pin=17)

if __name__ == "__main__":
    app = CatfeederMainApplication()