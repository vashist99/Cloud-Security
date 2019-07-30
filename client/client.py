import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 12345

s.connect((HOST,PORT))

f = open('pic2.png','rb')

while True:
    s.sendfile(f,0,None)
    break

#f.close()
s.close()