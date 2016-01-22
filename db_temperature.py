import datetime
import os
import sqlite3

class DbOperation(object):
    PATH = 'DBPATH'

    def __init__(self):
        self.con = sqlite3.Connection(os.environ.get(DbOperation.PATH))
        c = self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS temp(date text, time text, temp_c real)""")

    def insertRecord(self, temp):
        c = self.con.cursor()
        d = datetime.datetime.today()
        now_date = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
        now_time = str(d.hour) + ':' + str(d.second)
        c.execute("INSERT INTO temp(date, now_time, temp_c) VALUES(?, ?, ?)", (now_date, now_time, temp))
        self.con.commit()

    def connectionClose(self):
        self.con.close()
