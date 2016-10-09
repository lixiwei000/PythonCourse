from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print("Connected from :",clnt)

    def dataReceived(self, data):
        self.transport.write(bytes("[%s] %s" % (ctime(),str(data,"utf8")),"utf8"))

factory = protocol.Factory()
factory.protocol = TSServerProtocol
print("Waiting for connection...")
reactor.listenTCP(PORT,factory)
reactor.run()
