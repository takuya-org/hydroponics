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
    PWM = 17

    def __init__(self):
	    Motor.GPIO.setFunction(Motor.MOTORA_1, Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.MOTORA_2, Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.MOTORB_1, Motor.GPIO.OUT)
    	Motor.GPIO.setFunction(Motor.MOTORB_2, Motor.GPIO.OUT)
    	Motor.GPIO.setFunction(Motor.PWM, Motor.GPIO.OUT)
    	Motor.GPIO.digitalWrite(Motor.PWM, Motor.GPIO.HIGH)

    def forward(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.HIGH)
        time.sleep(2)
        Motor.stop()

    def back(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.LOW)
        time.sleep(2)
        Motor.stop()

    def stop(self):
        Motor.GPIO.digitalWrite(Motor.MOTORA_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORA_2, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_1, Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.MOTORB_2, Motor.GPIO.LOW)

# motor = Motor()
# def setup():
#     pass

# def loop():
#     motor.forward()
#     time.sleep(2)