import socket
from Crypto.PublicKey import RSA

#generating key obj
tup = RSA.generate(bits=2048,e=65537)

HOST = '127.0.0.1'
PORT = 56376
PORT1 = 12345

#listening and accepting connection from client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
c,addr = s.accept()
print('connected to client')

#listening and accepting connection from client1:
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((HOST,PORT1))
s1.listen(5)
c1,addr1 = s1.accept()
print('connected to client1 ')

#sending key object to client:
c.send(tup.exportKey('PEM'))
print('key object sent to client')

#recieving encrypted file from client
enc_data = c.recv(10000000) 
enc_file = open('enc_file.txt','wb')
enc_file.write(enc_data)
enc_file.close()
print('encrypted file recieved')

#decrypting file from client
f2 = open('enc_file.txt','rb')
data = f2.read()
data2 = RSA.pubkey.pubkey.decrypt(tup,data)
f2.close()
f = open('dec.txt','wb')
f.write(data2)
f.close()
print('file from client decrypted')

#recieving key object from client1:
tup1 = c1.recv(2048)
t = RSA.importKey(tup1)
print('key object recieved key object from client1')

#encrypting file again:
f = open('dec.txt','rb')
data = f.read()
f.close()
#encrypting 
enc_data = RSA.pubkey.pubkey.encrypt(t,data,3)
#storeD in enc_file.png
f2 = open('enc_file1.txt','wb')
f2.write(enc_data[0])
f2.close()
print('file encrypted')

#sending encrypted file:
f3 = open('enc_file1.txt','rb')
c1.sendfile(f3)
print('encrypted file sent to client1')






#recieving acknowledgment file:
ack_enc = c1.recv(100000000)
f = open('ack_enc.txt','wb')
f.write(ack_enc)
f.close()
print('ack recieved')

#decrypting acknowledgement file:
f2 = open('ack_enc.txt','rb')
data = f2.read()
data2 = RSA.pubkey.pubkey.decrypt(t,data)
f2.close()
f = open('ack_dec.txt','wb')
f.write(data2)
f.close()
print('ack decrypted')

#recieving key obj from client:
tup2 = c.recv(2048)
t2 = RSA.importKey(tup2)
print('recieved key obj from client')

#encrypting ack
f = open('ack_dec.txt','rb')
data = f.read()
f.close()
#encrypting 
enc_data = RSA.pubkey.pubkey.encrypt(t2,data,3)
#storeD in enc_file.png
f2 = open('ack.txt','wb')
f2.write(enc_data[0])
f2.close()
print('ack file encrypted')


#sending acknowledgement to client:
f2 = open('ack.txt','rb')
c.sendfile(f2)
f2.close()
print('ack sent to client')

c.close()
c1.close()