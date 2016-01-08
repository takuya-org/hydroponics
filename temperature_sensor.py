class Temperature(object):
    DIR = '/sys/bus/w1/devices/'
    DEVICE_NAME = '28-0115902811ff'
    FILE_NAME = '/w1_slave'

    def getTemprature(self):
        with open(Temperature.DIR + Temperature.DEVICE_NAME + Temperature.FILE_NAME) as f:
            data = f.read()
        temp = float(data[data.index('t=')+2:])/1000
        return temp
