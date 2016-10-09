from socket import *
from time import ctime


BUFFSIZE = 1024
ADDR = ("localhost",9000)

if __name__ == "__main__":
    udpSock = socket(AF_INET,SOCK_DGRAM)
    udpSock.bind(ADDR)
    while True:
        print("Waiting for data...")
        data,addr = udpSock.recvfrom(BUFFSIZE)
        data = str(data,encoding="utf8")
        print("Received from ",addr,":",data)
        udpSock.sendto(bytes("[%s] %s" % (ctime(),data),encoding="utf8"),addr)
    udpSock.close()