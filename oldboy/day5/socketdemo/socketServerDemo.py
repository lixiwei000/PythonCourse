import socketserver

class MySocketServer(socketserver.BaseRequestHandler):



    def setup(self):
        print("启动")

    def finish(self):
        print("结束")

    def handle(self):
        print(self.request,self.client_address,self.server)
        conn = self.request
        conn.send(b"Hello Client")
        while True:
            data = conn.recv(1024)
            print(str(data,encoding="utf-8"))
            send = input("To Client:")
            conn.send(bytes(send,encoding="utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('localhost',9995),MySocketServer)
    server.serve_forever()