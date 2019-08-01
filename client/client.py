import socket
import pyAesCrypt
#from os import stat,remove

#connecting to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 13579
s.connect((HOST,PORT))

#encrypting the file:
buffersize = 64*1024
password = "foopassword"
fin = open('new.png','rb')
fout = open('enc_file.png.aes','wb') 
pyAesCrypt.encryptStream(fin,fout,password,buffersize)
fout.close()
fin.close()

fout = open('enc_file.png.aes','rb')

k = password.encode('utf-8')
s.send(k)
print("password sent")

#sending encrypted file to server
while True:
    s.sendfile(fout,0,None)
    break
print("encrypted file sent")
#f2.close()
s.close()