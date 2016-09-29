import socketserver
import os
class MyFTPServer(socketserver.BaseRequestHandler):
    def finish(self):
        print("FTPServer 关闭")

    def handle(self):
        conn = self.request
        basePath = "/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day6/CloudFS"
        while True:
            fileInfo = str(conn.recv(1024),'utf8')
            operation,filename,filesize = fileInfo.split("|")
            if operation == "upload":
                receiveSize = 0
                fileDir = os.path.join(basePath,filename)
                f = open(fileDir,"wb")
                flag = True
                while flag:
                    if receiveSize < int(filesize):
                        data = conn.recv(1024)
                        f.write(data)
                        receiveSize += 1024
                    # 传输完毕,标志位复位
                    else:
                        receiveSize = 0
                        flag = False
                        f.close()
                        print("文件上传完毕:",fileInfo)
            elif operation == "download":
                fileDir = os.path.join(basePath,filename)# 找到需要被下载的文件
                f = open(fileDir,"rb")
                filesize = os.stat(fileDir).st_size# 被下载文件大小
                conn.send(bytes(str(filesize),"utf8")) # 将被下载文件大小返回给客户端

                sendSize = 0
                flag = True
                while flag:
                    if sendSize + 1024 < filesize:
                        data = f.read(1024)

                    else:
                        data = f.read(filesize - sendSize)
                        flag = False
                    conn.send(data)
                    sendSize += len(data)
                f.close()
            else:
                print("非法操作")
                continue
    def setup(self):
        print("FTPServer 启动")

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("localhost",9093 ),MyFTPServer)
    server.serve_forever()