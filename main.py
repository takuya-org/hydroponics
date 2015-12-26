import ControlMotor as motor
import lux
import time

class Main(object):
    def __init__(self):
        self.lux_sensor = lux.Lux()
        self.motor = motor.ControlMotor()

    def execute(self, interval_time):
        decision_list = self.lux_sensor.decision_direction()
        self.motor.movefromsensordata(decision_list)
        time.sleep(interval_time)

if __name__ == "__main__":
    main = Main()
    while True:
        main.execute(60*10) # 10分に1度
