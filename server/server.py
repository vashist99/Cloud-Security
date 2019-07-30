import socket

HOST = '127.0.0.1'

PORT = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
c,addr = s.accept()
print('connected by ',addr)

f = open('new.png','wb')

data = c.recv(100000)
#print(data[0],data[1],data[2],data[3])
#print(len(data))
f.write(data)
f.close

