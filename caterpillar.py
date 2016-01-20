import webiopi
import time

class Motor(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.GPIO = webiopi.GPIO
        self.PIN = {'MOTORA_1':22, 'MOTORA_2':27, 'MOTORB_1':23, 'MOTORB_2':24, 'PWM':18}
        #周波数
        self.PWM_FREQUENCY = 0.5
        self.GPIO.setFunction(self.PIN['MOTORA_1'], self.GPIO.OUT)
        self.GPIO.setFunction(self.PIN['MOTORA_2'], self.GPIO.OUT)
        self.GPIO.setFunction(self.PIN['MOTORB_1'], self.GPIO.OUT)
        self.GPIO.setFunction(self.PIN['MOTORB_2'], self.GPIO.OUT)
        self.GPIO.setFunction(self.PIN['PWM'], self.GPIO.PWM)
        self.GPIO.pwmWrite(self.PIN['PWM'], self.PWM_FREQUENCY)

    def forward(self):
        self.GPIO.digitalWrite(self.PIN['MOTORA_1'], self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.PIN['MOTORA_2'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORB_1'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORB_2'], self.GPIO.HIGH)
        time.sleep(3.8)
        self.stop()

    def back(self):
        self.GPIO.digitalWrite(self.PIN['MOTORA_1'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORA_2'], self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.PIN['MOTORB_1'], self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.PIN['MOTORB_2'], self.GPIO.LOW)
        time.sleep(3.8)
        self.stop()

    def turnLeft(self):
        self.GPIO.digitalWrite(self.PIN['MOTORA_1'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORA_2'], self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.PIN['MOTORB_1'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORB_2'], self.GPIO.HIGH)
        time.sleep(3.5)
        self.stop()

    def turnRight(self):
        self.GPIO.digitalWrite(self.PIN['MOTORA_1'], self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.PIN['MOTORA_2'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORB_1'], self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.PIN['MOTORB_2'], self.GPIO.LOW)
        time.sleep(3.5)
        self.stop()

    def stop(self):
        print("stop")
        self.GPIO.digitalWrite(self.PIN['MOTORA_1'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORA_2'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORB_1'], self.GPIO.LOW)
        self.GPIO.digitalWrite(self.PIN['MOTORB_2'], self.GPIO.LOW)
