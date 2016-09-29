'''
Client端
'''
import socket
from oldboy.day5.homework.utils.Constant import *
from oldboy.day5.homework.model.UserModel import User
from oldboy.day5.homework.service.UserService import UserService

def clientMain():
    username = input("Please input username:")
    password = input("Please input password:")
    user = User(username, password)
    userService = UserService()
    userId = userService.checkValidate(user)
    print(userId)

    if userId is not None:
        client = socket.socket()
        ip_port = ("localhost",9091)
        client.connect(ip_port)
        while True:
            data = client.recv(1024) # 这里也会阻塞
            print(str(data,encoding='utf-8'))
            send = input("To Server:")
            client.send(bytes(str(userId) + "#" + str(send), encoding='utf-8'))

if __name__ == "__main__":
    clientMain()