

import socket

sk = socket.socket()

ip_port = ("localhost",9995)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.send(b"Hello!")
    while True:
        print(str(conn.recv(1024),encoding='utf-8'))
        send = input("To Client:")
        conn.send(bytes(send,encoding='utf-8'))
    conn.close()