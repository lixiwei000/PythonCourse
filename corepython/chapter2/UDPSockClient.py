from socket import *
from time import ctime


BUFFSIZE = 1024
ADDR = ("localhost",9000)

if __name__ == "__main__":
    udpSockCli = socket(AF_INET,SOCK_DGRAM)
    while True:
        data = input(">")
        if not data:
            break
        data = bytes(data,encoding="utf8")
        udpSockCli.sendto(data,ADDR)
        data,addr = udpSockCli.recvfrom(BUFFSIZE)
        data = str(data,encoding="utf8")
        print(data)
    udpSockCli.close()