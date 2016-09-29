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
        # 上传文件
        if operation == "upload":
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
        elif operation == "download":
            baseDir = "/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day6/LocalFS"
            filename = filepath # 服务端文件名称
            fileDir = os.path.join(baseDir,filename) # 下载存储地址
            sk.send(bytes(str.format("{0}|{1}|{2}",operation,filename,0),"utf8")) # 首次发送需要下载的文件信息
            f = open(fileDir,"wb")
            receiveSize = 0
            flag = True # 文件接收结束标识
            filesize = sk.recv(1024)
            while flag:
                if receiveSize < int(filesize):
                    data = sk.recv(1024)
                    f.write(data)
                    receiveSize += 1024
                else:
                    receiveSize = 0
                    flag = False
                    print("下载文件结束",fileDir,filesize)
            f.close()
        else:
            print("非法操作!")
            continue
if __name__ == "__main__":
    main()






