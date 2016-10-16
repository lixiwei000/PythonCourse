import socket
import os

def main():
    ip_port = ("localhost", 9093)
    sk = socket.socket()
    sk.connect(ip_port)

    while True:
        fileInfo = input("Tell me the operation|filepath that you wanna to upload:")
        operation,filepath = fileInfo.split("|")
        filename = os.path.basename(filepath)
        filesize = os.stat(filepath).st_size
        sk.send(bytes(str.format("{0}|{1}|{2}",operation,filename,filesize),"utf8"))
        sendSize = 0
        flag = True;
        f = open(filepath,"rb")
        while flag:
            if sendSize + 1024 < filesize:
                data = f.read(1024)
            else:
                data = f.read(filesize - sendSize)
                flag = False
            sk.send(data)
            sendSize += len(data)
        f.close()

if __name__ == "__main__":
    main()






