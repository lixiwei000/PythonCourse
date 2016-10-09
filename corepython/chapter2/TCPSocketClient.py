
from socket import *
from time import ctime

HOST = "localhost"
PORT = 9000
BUFFSIZE = 1024
ADDR = (HOST,PORT)

if __name__ == "__main__":
    tcpSockClient = socket(AF_INET,SOCK_STREAM)
    tcpSockClient.connect(ADDR)

    while True:
        data = input(">")
        if not data:
            print("Client want to close connection...")
            break
        tcpSockClient.send(bytes(data,"utf8"))
        data = tcpSockClient.recv(BUFFSIZE)
        print(str(data,encoding="utf8"))

    tcpSockClient.close()