import socket
from Crypto.PublicKey import RSA
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import time

#generating key obj
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    backend=default_backend()
)
public_key = private_key.public_key()
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

#connecting to server:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '146.51.240.117.in-addr.arpa'
PORT = 8080
s.connect((HOST,PORT))
print('connected to server',HOST)

for i in range(20):
    #sending key object to server:
    s.sendall(pem)
    #print('key object sent to server')

    #recieving file from server:
    enc_data = s.recv(10000000) 
    enc_file = open('enc_file.txt','wb')
    enc_file.write(enc_data)
    enc_file.close()
    #print('encrypted file recieved')

    #decrypting file:
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
    f = open('final.txt','wb')
    f.write(data2)
    f.close()
    #print('file from server decrypted')




    #encrypting acknowledgement
    #recieve public key of server
    server_public_key = serialization.load_pem_public_key(
        s.recv(2048),
        backend=default_backend())
    #print('server public_key recieved')
    f = open('ack.txt','rb')
    data = f.read()
    f.close()
    enc_data = server_public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    #storeD in ack_enc.txt
    f2 = open('ack_enc.txt','wb')
    f2.write(enc_data)
    f2.close()
    #print('file encrypted')

    #sending acknowledgement:
    f = open('ack_enc.txt','rb')
    s.sendfile(f)
    f.close()

s.close()


