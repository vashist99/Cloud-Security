import socket
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RSAImplementation
#from os import stat,remove

#connecting to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 56378
s.connect((HOST,PORT))

#encrypting the file:
tup = RSA.generate(bits=2048,e=65537)
s.send(tup.exportKey('PEM'))


f = open('answers.txt','rb')
data = f.read()
f.close()
#encrypting new.png
enc_data = RSA.pubkey.pubkey.encrypt(tup,data,3)
#print(enc_data)

#storeD in enc_file.png
f2 = open('enc_file.txt','wb')
f2.write(enc_data[0])
f2.close()

f2 = open('enc_file.txt','rb')

s.sendfile(f2)
print('encrypted file sent')

f2.close()

s.close()