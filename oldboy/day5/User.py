from oldboy.day5.SqlHelper import SqlHelper

class User(object):
    def __init__(self,username,password):
        self.__sqlHelper = SqlHelper()
        self.username = username
        self.password = password

    def checkValidate(self):
        sql = "select * from tb_user where username = %s and password = %s"
        params = (self.username,self.password)
        result = self.__sqlHelper.findOne(sql,params)
        # self.__sqlHelper.closeConn()
        if result is not None:
            return True
        else:
            return False
    def selectAll(self):
        sql = "select  * from tb_user"
        result = self.__sqlHelper.findAll(sql,None)
        # self.__sqlHelper.closeConn()
        return result

    def __del__(self):
        self.__sqlHelper.closeConn()
