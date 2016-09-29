import mysql.connector
from oldboy.day5.config import *
class SqlHelper(object):
    def __init__(self):
        try:
            self.__connDict = connDict
            self.conn = mysql.connector.connect(**self.__connDict)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库连接失败")
            print(e)

    def findAll(self,sql,params):
        self.cursor.execute(sql,params)
        result = self.cursor.fetchall()
        return result

    def findOne(self,sql,params):
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()
        return result

    def closeConn(self):
        self.cursor.close()
        self.conn.close()