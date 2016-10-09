from socket import *

BUFFSIZE = 1024
ADDR = ("localhost",9001)

while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input(">")
    if not data:
        break

    tcpCliSock.send(bytes("%s\r\n" % data,"utf8"))
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break
    data = str(data,"utf8")
    print(data.strip())
    tcpCliSock.close()