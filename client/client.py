import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 12345

s.connect((HOST,PORT))

#f = open('pic2.png','rb')
#l = f.read()
while True:
    s.send(b'Hello! we are connected')
    #s.send(f.read())
    break

print(s.recv(1024))

#f.close()
s.close()