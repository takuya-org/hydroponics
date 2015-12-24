import spidev

class Sensor(object):

    def __init__(self):
        spi = spidev.SpiDev()
        spi.open(0,0)

    def read_channel(self,channel):
        """
        MCP3008経由でアナログセンサからのデータを受け取る。
        channelはMCP3008の入力チャンネルで、0から7の値
        # """
        # adc = self.spi.xfer2([1,(8+channel)<<4,0])
        # data = ((adc[1]&3) << 8)     + adc[2]
        # return data
