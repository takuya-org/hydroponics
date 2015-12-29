class Temperature(object):
	DIR = '/sys/bus/w1/devices/'
	DEVICE_NAME = ''
	FILE_NAME = '/w1_slave'

    def __init__(self):
        pass

    def getTemprature(self):
        with open(DIR + DEVICE + FILE_NAME) as f:
            data = f.read()
        temp = float(data[data.index('t=')+2:])/1000
        return temp
