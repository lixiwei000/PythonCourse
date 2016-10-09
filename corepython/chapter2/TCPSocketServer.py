'''
网络编程
TCP:基于连接的通信。三次握手、基于数据流、数据可靠性搞高、数据有序
UDP:无连接通信。基于报文、数据可靠性低、系统资源占用少、数据无序
'''

from socket import *
from time import ctime

HOST = "localhost"
PORT = 9000
BUFFSIZE = 1024
ADDR = (HOST,PORT)

if __name__ == "__main__":
    tcpSock = socket(AF_INET,SOCK_STREAM)
    # udpSock = socket(AF_INET,SOCK_DGRAM)
    tcpSock.bind(ADDR)
    tcpSock.listen(5)

    while True:
        print("Waiting for connection...")
        recvSock,addr = tcpSock.accept()
        print("Connection established...")
        while True:
            data = recvSock.recv(BUFFSIZE)
            data = str(data,encoding="utf8")
            if not data:
                print("Connection closed...")
                break
            recvSock.send(bytes("[%s] %s " % (ctime(),data),"utf8"))
        recvSock.close()
    tcpSock.close()
