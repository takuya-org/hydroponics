import ControlMotor as motor
import temperature_sensor as temperature
import lux
import time
import enum


class Main(object):
    PatternFunc = enum.Enum("PatternFunc", "read maybe_motor")

    def __init__(self, execute_queue):
        self.lux_sensor = lux.Lux()
        self.motor = motor.ControlMotor()
        self.exe_q = execute_queue
        self.temp_sensor = temperature.Temperature()

    def execute(self, interval_sec):
        for exe in self.exe_q:
            if exe is Main.PatternFunc.read:
                self._sensor_read_store()
            elif exe is Main.PatternFunc.maybe_motor:
                self._read_exec_motor()
            else:
                pass
            time.sleep(interval_sec)

    def _sensor_read_store(self):
        self.lux_sensor.get_average()

    def _read_exec_motor(self):
        self.temp_sensor.storeTemperatureData()
        decision_list = self.lux_sensor.decision_direction()
        print(decision_list)
        if len(decision_list) > 0:
            self.motor.movefromsensordata(decision_list)


if __name__ == "__main__":
    exe_q = (
        Main.PatternFunc.read,
        Main.PatternFunc.read,
        Main.PatternFunc.read,
        Main.PatternFunc.read,
        Main.PatternFunc.read,
        Main.PatternFunc.maybe_motor
    )

    main = Main(exe_q)
    while True:
        main.execute(60 * 10)  # 10分に1度
