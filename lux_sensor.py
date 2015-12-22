#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
class Lux(object):

    def __init__(self):
        self.set_value()
    def read_channel(self,channel):
        """
        MCP3008経由でアナログセンサからのデータを受け取る。
        channelはMCP3008の入力チャンネルで、0から7の値
        # """
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8)     + adc[2]
        return data

    def set_value(self):
        self.cds0 = self.read_channel(0)
        self.cds1 = self.read_channel(1)
        self.cds2 = self.read_channel(2)
        self.cds3 = self.read_channel(3)

    def decision_move(self):
        self.set_value()
        self.lux_list = {"cds0":self.cds0,
                         "cds1":self.cds1,
                         "cds2":self.cds2,
                         "cds3":self.cds3}
        print(self.lux_list)
        max_lux = max(self.lux_list, key=(lambda x: self.lux_list[x]))
        if max_lux == "cds0":
          return [2,4,2]
        elif max_lux == "cds1":
          return [2,6,2]
        elif max_lux == "cds2":
          return [8,4,8]
        elif max_lux == "cds3":
          return [8,6,8]

    def get_avg(self):
        self.set_value()
        print(self.cds0)
        print(self.cds1)
        print(self.cds2)
        print(self.cds3)
        return (self.cds0+self.cds1+self.cds2+self.cds3)/4





    ###まーくんのうんこーど###
    #   hoge = min(cds0,cds1,cds2,cds3)   #最小値メモ　他との比較で使う用のやつ
    #   print "最小値：%s" % hoge
    #
     #一番明るいのがどれかの判定　
      # if hoge == cds0 :
      #   print "左前 最小値：%s" % hoge
      # if hoge == cds1 :
      #   print "右前 最小値：%s" % hoge
      # if hoge == cds2 :
      #   print "左後 最小値：%s" % hoge
      # if hoge == cds3 :
      #   print "右後 最小値：%s" % hoge
      #   print ""
      #

      #test