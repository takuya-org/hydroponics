import webiopi
import time
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
PWMA = 17
PWMB = 18

def setup():
    GPIO.setFunction(MOTORA_1, GPIO.OUT)
    GPIO.setFunction(MOTORA_2, GPIO.OUT)
    GPIO.setFunction(MOTORB_1, GPIO.OUT)
    GPIO.setFunction(MOTORB_2, GPIO.OUT)

def loop():
	#なんか
	forward()
	webiopi.sleep(5)
	back()
	webiopi.sleep(5)
	turnLeft()
	webiopi.sleep(5)
	turnRight()
	webiopi.sleep(5)

def forward():
	GPIO.digitalWrite(MOTORA_1, GPIO.HIGH)
	GPIO.digitalWrite(MOTORA_2, GPIO.LOW)
	GPIO.digitalWrite(MOTORB_1, GPIO.LOW)
	GPIO.digitalWrite(MOTORB_2, GPIO.HIGH)

def back():
	GPIO.digitalWrite(MOTORA_1, GPIO.LOW)
	GPIO.digitalWrite(MOTORA_2, GPIO.HIGH)
	GPIO.digitalWrite(MOTORB_1, GPIO.HIGH)
	GPIO.digitalWrite(MOTORB_2, GPIO.LOW)

def turnLeft():
	GPIO.digitalWrite(MOTORA_1, GPIO.HIGH)
	GPIO.digitalWrite(MOTORA_2, GPIO.LOW)
	GPIO.digitalWrite(MOTORB_1, GPIO.HIGH)
	GPIO.digitalWrite(MOTORB_2, GPIO.LOW)

def turnRight():
	GPIO.digitalWrite(MOTORA_1, GPIO.LOW)
	GPIO.digitalWrite(MOTORA_2, GPIO.HIGH)
	GPIO.digitalWrite(MOTORB_1, GPIO.LOW)
	GPIO.digitalWrite(MOTORB_2, GPIO.HIGH)

def stop():
	GPIO.digitalWrite(MOTORA_1, GPIO.LOW)
	GPIO.digitalWrite(MOTORA_2, GPIO.LOW)
	GPIO.digitalWrite(MOTORB_1, GPIO.LOW)
	GPIO.digitalWrite(MOTORB_2, GPIO.LOW)