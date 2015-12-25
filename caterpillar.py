import webiopi
import time

class Motor:
    GPIO = webiopi.GPIO
    #モーター１赤
    MOTORA_1 = 22
    #モーター１黒
    MOTORA_2 = 27
    #モーター２赤
    MOTORB_1 = 23
    #モーター２黒
    MOTORB_2 = 24
    #PWM
    PWM = 18

    def __init__(self):
        Motor.GPIO.setFunction(Motor.MOTORA_1, Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.MOTORA_2, Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.MOTORB_1, Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.MOTORB_2, Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.PWM, Motor.GPIO.PWM)
        Motor.GPIO.pwmWrite(Motor.PWM, 0.05)

    def forward(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.HIGH)
        time.sleep(0.9)
        Motor.stop(Motor)

    def back(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.LOW)
        time.sleep(0.9)
        Motor.stop(Motor)

    def turnLeft(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.LOW)
        time.sleep(0.5)
        Motor.stop(Motor)

    def turnRight(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.HIGH)
        time.sleep(0.5)
        Motor.stop(Motor)

    def stop(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.LOW)

motor = Motor()
def setup():
    pass

def loop():
    # motor.forward()
    # time.sleep(5)
    # motor.back()
    # time.sleep(5)
    motor.turnLeft()
    time.sleep(5)
    motor.turnRight()
    time.sleep(5)