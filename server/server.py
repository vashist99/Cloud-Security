import socket
from Crypto.PublicKey import RSA
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import time


#generating public and prvate key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    backend=default_backend()
)
public_key = private_key.public_key()
#public key serialization
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


HOST = '127.0.0.1'
PORT = 56377
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


for i in range(20):
    #sending key object to client:
    c.sendall(pem)
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
    data2 = private_key.decrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    f2.close()
    f = open('dec.txt','wb')
    f.write(data2)
    f.close()
    print('file from client decrypted')

    #recieving key object from client1:
    client1_public_key = public_key = serialization.load_pem_public_key(
        c1.recv(2048),
        backend=default_backend())
    print('key object recieved key object from client1')

    #encrypting file again:
    f = open('dec.txt','rb')
    data = f.read()
    f.close()
    #encrypting 
    enc_data = client1_public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    #storeD in enc_file.png
    f2 = open('enc_file1.txt','wb')
    f2.write(enc_data)
    f2.close()
    print('file encrypted')

    #sending encrypted file:
    f3 = open('enc_file1.txt','rb')
    c1.sendfile(f3)
    print('encrypted file sent to client1')





    #send public key to client 1:
    c1.sendall(pem)
    print('public key sent to client1')
    #recieving acknowledgment file:
    ack_enc = c1.recv(100000000)
    f = open('ack_enc.txt','wb')
    f.write(ack_enc)
    f.close()
    print('ack recieved')

    #decrypting acknowledgement file:
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
    f = open('ack_dec.txt','wb')
    f.write(data2)
    f.close()
    print('ack decrypted')

    #recieving key obj from client:
    client_public_key = serialization.load_pem_public_key(
        c.recv(2048),
        backend=default_backend()
    )

    print('recieved key obj from client')

    #encrypting ack
    f = open('ack_dec.txt','rb')
    data = f.read()
    f.close()
    #encrypting 
    enc_data = client_public_key.encrypt(
        data,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    #storeD in enc_file.png
    f2 = open('ack.txt','wb')
    f2.write(enc_data)
    f2.close()
    print('ack file encrypted')

    #sending acknowledgement to client:
    f2 = open('ack.txt','rb')
    c.sendfile(f2)
    f2.close()
    print('ack sent to client')

c.close()
c1.close()