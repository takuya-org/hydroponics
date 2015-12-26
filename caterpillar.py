import webiopi
import time

class Motor:
    GPIO = webiopi.GPIO
    PIN = {'MOTORA_1':22, 'MOTORA_2':27, 'MOTORB_1':23, 'MOTORB_2':24, 'PWM':18}
    #周波数
    PWM_FREQUENCY = 0.05

    def __init__(self):
        Motor.GPIO.setFunction(Motor.PIN['MOTORA_1'], Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.PIN['MOTORA_2'], Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.PIN['MOTORB_1'], Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.PIN['MOTORB_2'], Motor.GPIO.OUT)
        Motor.GPIO.setFunction(Motor.PIN['PWM'], Motor.GPIO.PWM)
        Motor.GPIO.pwmWrite(Motor.PIN['PWM'], Motor.PWM_FREQUENCY)

    def forward(self):
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_1'], Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_2'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_1'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_2'], Motor.GPIO.HIGH)
        time.sleep(0.9)
        Motor.stop(Motor)

    def back(self):
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_1'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_2'], Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_1'], Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_2'], Motor.GPIO.LOW)
        time.sleep(0.9)
        Motor.stop(Motor)

    def turnLeft(self):
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_1'], Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_2'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_1'], Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_2'], Motor.GPIO.LOW)
        time.sleep(0.5)
        Motor.stop(Motor)

    def turnRight(self):
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_1'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_2'], Motor.GPIO.HIGH)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_1'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_2'], Motor.GPIO.HIGH)
        time.sleep(0.5)
        Motor.stop(Motor)

    def stop(self):
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_1'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORA_2'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_1'], Motor.GPIO.LOW)
        Motor.GPIO.digitalWrite(Motor.PIN['MOTORB_2'], Motor.GPIO.LOW)
