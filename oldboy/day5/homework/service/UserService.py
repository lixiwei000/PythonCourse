from oldboy.day5.homework.model.UserModel import User
from oldboy.day5.homework.utils.SqlHelper import SqlHelper
import time


class UserService(object):
    def __init__(self):
        self.sqlHelper = SqlHelper()

    def checkValidate(self, user):
        sql = "select * from tb_user where username = %s and password = %s"
        params = (user.username, user.password)
        userList = self.sqlHelper.findAll(sql, params)
        if len(userList) > 0:
            print("登陆成功,欢迎您进入聊天系统 ", userList[0][1])
            return userList[0][0]
        else:
            print("用户名或密码错误")
            return None

    def saveChat(self, userid, content):
        sql = "insert into tb_chat(userid,content,createtime) values(%s,%s,%s)"
        params = (userid, content, time.strftime("%Y-%m-%d %H:%M:%S"))
        self.sqlHelper.addChatRecord(sql, params)
