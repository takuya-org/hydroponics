#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sensor
from functools import reduce


class Lux(object):
    def __init__(self):
        self.s = sensor.Sensor()
        self.read_sensor_value()
        self.average_list = []

    def read_sensor_value(self):
        self.cds0 = self.s.read_channel(0)
        self.cds1 = self.s.read_channel(1)
        self.cds2 = self.s.read_channel(2)
        self.cds3 = self.s.read_channel(3)

    def decision_direction(self):
        self.read_sensor_value()
        self.lux_list = {
            "cds0": self.cds0,
            "cds1": self.cds1,
            "cds2": self.cds2,
            "cds3": self.cds3
        }
        print(self.lux_list)
        max_lux = min(self.lux_list, key=(lambda x: self.lux_list[x]))

        lux_val_ave = self.pop_average_value()

        # 平均より暗くなってなければ
        if not self.lux_list[max_lux] > lux_val_ave:
            return ()

        if max_lux == "cds0":
            return [2, 4, 2]
        elif max_lux == "cds1":
            return [2, 6, 2]
        elif max_lux == "cds2":
            return [8, 4, 8]
        elif max_lux == "cds3":
            return [8, 6, 8]

    def get_average(self):
        self.read_sensor_value()
        print(self.cds0)
        print(self.cds1)
        print(self.cds2)
        print(self.cds3)
        sensor_ave = (self.cds0 + self.cds1 + self.cds2 + self.cds3) / 4
        self.store_average_value(sensor_ave)
        return sensor_ave

    def store_average_value(self, val):
        # dbに変更したりするかも
        self.average_list.append(val)

    def pop_average_value(self):
        sum_val = reduce(lambda a, b: a + b, self.average_list)
        list_length = len(self.average_list)
        self.average_list = []  # 次のイテレーションに向けて初期化
        return sum_val / list_length


        ###まーくんのうんこーど###
        #   hoge = min(cds0,cds1,cds2,cds3)   #最小値メモ　他との比較で使う用のやつ
        #   print "最小値：%s" % hoge
        #
        # 一番明るいのがどれかの判定
        # if hoge == cds0 :
        #   print "左前 最小値：%s" % hoge
        # if hoge == cds1 :
        #   print "右前 最小値：%s" % hoge
        # if hoge == cds2 :
        #   print "左後 最小値：%s" % hoge
        # if hoge == cds3 :
        #   print "右後 最小値：%s" % hoge
        #   print ""
