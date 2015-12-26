import ControlMotor as motor
import lux
import time

class Main(object):
    def __init__(self):
        self.lux_sensor = lux.Lux()
        self.motor = motor.ControlMotor()

    def execute(self, interval_time):
        direction_list = self.lux_sensor.dicision_direction()
        self.motor.movefromsensordata(direction_list)
        time.sleep(interval_time)

if __name__ == "__main__":
    main = Main()
    while True:
        main.execute(60*10) # 10分に1度
