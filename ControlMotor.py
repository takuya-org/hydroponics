import time
import caterpillar

class ControlMotor:
    def __init__(self):
        self.motor = caterpillar.Motor()

    def move(self, list):
        for item in list:
            if item == 2:
                self.motor.forward()
            if item == 4:
                self.motor.turnLeft()
            if item == 6:
                self.motor.turnRight()
       	    if item == 8:
       	        self.motor.back()
       	    time.sleep(1)
