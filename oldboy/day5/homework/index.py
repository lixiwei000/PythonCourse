'''
需求分析:
    1. 三层架构
    2. 聊天记录存储到Mysql
    3. 采用Socket接收和发送聊天数据
    4. 要可以查看聊天记录的功能
'''


from oldboy.day5.homework.utils.ChatServer import MySocketServer
from oldboy.day5.homework.utils.Constant import *
import socketserver
import socket

def main():
    # 启动SocketServer
    server = socketserver.ThreadingTCPServer(("localhost", 9091), MySocketServer)
    server.serve_forever()

if __name__ == "__main__":
    main()
