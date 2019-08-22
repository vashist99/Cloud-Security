import socket
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RSAImplementation
import time
#from os import stat,remove

sum=0

#generating key obj
tup = RSA.generate(bits=2048,e=65537)




#connecting to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 56377
s.connect((HOST,PORT))
print('connected to server')

for i in range(20):
    temp=0
    #timer started:
    start_time = time.time()
    #recieving key object from server:
    tups = s.recv(2048)
    ts = RSA.importKey(tups)
    print('key object recieved key object from server')


    #encrypting the file:
    f = open('answers.txt','rb')
    data = f.read()
    f.close()
    #encrypting new.png
    enc_data = RSA.pubkey.pubkey.encrypt(ts,data,3)
    #storeD in enc_file.png
    f2 = open('enc_file.txt','wb')
    f2.write(enc_data[0])
    f2.close()
    print('file encrypted')

    #sending file to server:
    f2 = open('enc_file.txt','rb')
    s.sendfile(f2)
    print('encrypted file sent')
    f2.close()




    #sending key obj to server:
    s.send(tup.exportKey('PEM'))
    print('key object sent to server')

    #recieving acknowledgement from server:
    ack_enc = s.recv(10000000) 
    ackf = open('ack_enc.txt','wb')
    ackf.write(ack_enc)
    ackf.close()
    print('encrypted ack file recieved')

    #decrypting ack file:
    f2 = open('ack_enc.txt','rb')
    data = f2.read()
    data2 = RSA.pubkey.pubkey.decrypt(tup,data)
    f2.close()
    f = open('final.txt','wb')
    f.write(data2)
    f.close()
    print('ack decrypted')
    #end timer
    end_time = time.time()
    temp = (end_time-start_time)
    sum += temp


s.close()



print('average time taken for 10 iteration for this file size ',sum/10)