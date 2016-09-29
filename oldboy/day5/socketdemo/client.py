import socket

client = socket.socket()
ip_port = ("localhost",9995)
client.connect(ip_port)
while True:
    data = client.recv(1024) # 这里也会阻塞
    print(str(data,encoding='utf-8'))
    send = input("To Server:")
    client.send(bytes(send,encoding='utf-8'))