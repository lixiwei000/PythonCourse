import mysql.connector
from oldboy.day5.homework.utils.Constant import *
class SqlHelper(object):
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**connStr)
            self.cursor = self.conn.cursor()
            print("连接数据库成功")
        except Exception as e:
            print("连接数据库异常:",e)

    def findAll(self,sql,params):
        self.cursor.execute(sql,params)
        result = self.cursor.fetchall()
        return result

    def addChatRecord(self,sql,params):
        try:
            self.cursor.execute(sql,params)
            self.conn.commit()
        except Exception as e:
            print("插入聊天记录失败 ",e)

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("数据库连接已关闭s")
