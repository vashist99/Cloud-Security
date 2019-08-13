import socket
from Crypto.PublicKey import RSA

from os import stat,remove

#listening and accepting connection
HOST = '127.0.0.1'
PORT = 56378
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
c,addr = s.accept()
print('connected by ',addr)

tup = c.recv(2048)
t = RSA.importKey(tup)

#recieving encrypted file 
enc_data = c.recv(10000000) #recieving key
enc_file = open('enc_file.txt','wb')
enc_file.write(enc_data)
enc_file.close()
print('encrypted file recieved')

#decrypting
f2 = open('enc_file.txt','rb')
data = f2.read()
data2 = RSA.pubkey.pubkey.decrypt(t,data)
f2.close()
f = open('final.txt','wb')
f.write(data2)
f.close()

s.close()
c.close()