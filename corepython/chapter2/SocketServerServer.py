from socketserver import TCPServer as TCP,StreamRequestHandler as SRH
from time import ctime

ADDR = ("localhost",9001)

class MyRequestHandler(SRH):
    def handle(self):
        print("Connected from",self.client_address)
        data = str(self.rfile.readline(),"utf8")
        print("Received :",data)
        self.wfile.write(bytes("[%s] %s" % (ctime(),data),encoding="utf8"))

if __name__ == "__main__":
    tcpServ = TCP(ADDR,MyRequestHandler)
    print("Waiting for connection...")
    tcpServ.serve_forever()