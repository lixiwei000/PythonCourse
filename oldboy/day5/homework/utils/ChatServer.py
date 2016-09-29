import socketserver
from oldboy.day5.homework.service.UserService import UserService

class MySocketServer(socketserver.BaseRequestHandler):
    def setup(self):
        print("ChatRoom Server is opening...")

    def finish(self):
        print("ChartRoom Server is closing...")

    def handle(self):
        conn = self.request
        conn.send(b'Hello , my name is Mr.Robot')
        self.userService = UserService()
        while True:
            data = str(conn.recv(1024),encoding='utf8')
            print("Server Receive:",data)
            userId = data.split('#')[0]
            content = data.split('#')[1]
            self.userService.saveChat(userId,content)
            callback = "你tm说啥的SB"
            if content.__contains__("你好"):
                callback = "你好啊,愚蠢的人类"
            elif content.__contains__("傻逼"):
                callback = "你他妈才傻逼呢"
            conn.send(bytes(callback,encoding='utf8'))