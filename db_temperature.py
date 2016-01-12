import datetime
import sqlite3
class db_operation(object):
    DIR = ''
    FILE_NAME = 'hydroponics.db'

    def __init__(self):
        self.con = sqlite3.Connection(db_operation.DIR + db_operation.FILE_NAME)
        c = self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS temp(date text, temp_c real, PRIMARY KEY(date))""")

    def insertRecord(self, temp):
        c = self.con.cursor()
        d = datetime.datetime.today()
        now_date = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
        c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", (now_date, temp))
        self.con.commit()

    def connectionClose():
        self.con.close()
