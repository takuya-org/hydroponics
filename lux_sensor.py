#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0,0)

def read_channel(channel):
  """
  MCP3008経由でアナログセンサからのデータを受け取る。
  channelはMCP3008の入力チャンネルで、0から7の値
  """
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
def decision_move(max_lux):
  if max_lux == "cds0":
    return [2,4,2]
  elif max_lux == "cds1":
    return [2,6,2]
  elif max_lux == "cds2":
    return [8,4,8]
  elif max_lux == "cds3":
    return [8,6,8]



while True:

  cds0 = read_channel(0)
  cds1 = read_channel(1)
  cds2 = read_channel(2)
  cds3 = read_channel(3)
  lux = {"cds0":cds0,
         "cds1":cds1,
         "cds2":cds2,
         "cds3":cds3}
  max_lux = max(lux, key=(lambda x: lux[x]))

  print(lux)
  print(max_lux)
  print (decision_move(max_lux))







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
  time.sleep(100)
