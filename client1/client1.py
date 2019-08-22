import socket
from Crypto.PublicKey import RSA
import time

#generating key obj
tup = RSA.generate(bits=2048,e=65537)

#connecting to server:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 12345
s.connect((HOST,PORT))
print('connected to server')

for i in range(20):
    #sending key object to server:
    s.send(tup.exportKey('PEM'))
    print('key object sent to server')

    #recieving file from server:
    enc_data = s.recv(10000000) 
    enc_file = open('enc_file.txt','wb')
    enc_file.write(enc_data)
    enc_file.close()
    print('encrypted file recieved')

    #decrypting file:
    f2 = open('enc_file.txt','rb')
    data = f2.read()
    data2 = RSA.pubkey.pubkey.decrypt(tup,data)
    f2.close()
    f = open('final.txt','wb')
    f.write(data2)
    f.close()
    print('file from server decrypted')




    #encrypting acknowledgement
    f = open('ack.txt','rb')
    data = f.read()
    f.close()
    enc_data = RSA.pubkey.pubkey.encrypt(tup,data,3)
    #storeD in ack_enc.txt
    f2 = open('ack_enc.txt','wb')
    f2.write(enc_data[0])
    f2.close()
    print('file encrypted')

    #sending acknowledgement:
    f = open('ack_enc.txt','rb')
    s.sendfile(f)
    f.close()

s.close()


