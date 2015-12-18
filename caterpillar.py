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

    GPIO.setFunction(MOTORA_1, GPIO.OUT)
    GPIO.setFunction(MOTORA_2, GPIO.OUT)
    GPIO.setFunction(MOTORB_1, GPIO.OUT)
    GPIO.setFunction(MOTORB_2, GPIO.OUT)
    GPIO.setFunction(PWM, GPIO.OUT)
    GPIO.digitalWrite(PWM, GPIO.HIGH)

    def forward(self):
        self.GPIO.digitalWrite(self.MOTORA_1, self.GPIO.HIGH)
        self.GPIO.digitalWrite(self.MOTORA_2, self.GPIO.LOW)
        self.GPIO.digitalWrite(self.MOTORB_1, self.GPIO.LOW)
        self.GPIO.digitalWrite(self.MOTORB_2, self.GPIO.HIGH)
        time.sleep(2)
        self.stop()

    def stop(self):
        self.GPIO.digitalWrite(self.MOTORA_1, self.GPIO.LOW)
        self.GPIO.digitalWrite(self.MOTORA_2, self.GPIO.LOW)
        self.GPIO.digitalWrite(self.MOTORB_1, self.GPIO.LOW)
        self.GPIO.digitalWrite(self.MOTORB_2, self.GPIO.LOW)

motor = Motor()
def setup():
    pass

def loop():
    motor.forward()
    time.sleep(2)