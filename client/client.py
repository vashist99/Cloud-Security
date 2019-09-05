import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
#from Crypto.PublicKey import RSA
#from Crypto.PublicKey.RSA import RSAImplementation
import cryptography
import time
#from os import stat,remove

sum=0

#generating public and private key
private_key = rsa.generate_private_key(public_exponent = 65537,key_size = 4096,backend = default_backend())
public_key = private_key.public_key()
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


#def encryption()



#connecting to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 56376
s.connect((HOST,PORT))
print('connected to server')

for i in range(20):
    temp=0
    #timer started:
    start_time = time.time()
    #recieving key and deserializing from server:
    server_public_key = serialization.load_pem_public_key(
        s.recv(2048),
        backend=default_backend()
    )

    
    #print('key recieved key object from server')

    #encrypting the file:
    f = open('answers.txt','rb')
    data = f.read()
    f.close()
    #encrypting new.png
    enc_data = server_public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    #storeD in enc_file.png
    f2 = open('enc_file.txt','wb')
    f2.write(enc_data)
    f2.close()
    #print('file encrypted')

    #sending file to server:
    f2 = open('enc_file.txt','rb')
    s.sendfile(f2)
    #print('encrypted file sent')
    f2.close()




    #sending key obj to server:
    s.sendall(pem)
    #print('key object sent to server')

    #recieving acknowledgement from server:
    ack_enc = s.recv(10000) 
    ackf = open('ack_enc.txt','wb')
    ackf.write(ack_enc)
    ackf.close()
    #print('encrypted ack file recieved')

    #decrypting ack file:
    f2 = open('ack_enc.txt','rb')
    data = f2.read()
    data2 = private_key.decrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    f2.close()
    f = open('final.txt','wb')
    f.write(data2)
    f.close()
    #print('ack decrypted')
    #end timer
    end_time = time.time()
    temp = (end_time-start_time)
    sum += temp


s.close()



print('average time taken for 10 iteration for this file size ',sum/10)