import socket
import pyAesCrypt
from os import stat

#listening and accepting connection
HOST = '127.0.0.1'
PORT = 13579
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
c,addr = s.accept()
print('connected by ',addr)

k = c.recv(1024) #recieving key
password = k.decode('utf-8')
print('password recieved')
buffersize = 64*1024

data = c.recv(10000000)
f = open('enc_file.png.aes','wb')
f.write(data)
f.close()
print('encrypted file recieved')

encFileSize = stat("enc_file.png").st_size

f1 = open('enc_file.png.aes','rb')
f2 = open('final.png','wb')
pyAesCrypt.decryptStream(f1,f2,password,buffersize,encFileSize)

s.close()