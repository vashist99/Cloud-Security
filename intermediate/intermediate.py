import socket
from Crypto.Cipher import AES
import time


#assigning shared key with server
key_s = b'T\x91\x86\xe6\xa3\x19\xb4\x10~\xc3\xe9\xcf\t\xa3\xec\xd8'
iv_s = b'A]L\x93\xb4\xae\xbc\xd7\xa0\xf4\xa9\xd7\xee2Y\x0c'

#assigning shared key with client
key_c = b'[\xfb?\t\xd1#|\xdeQ\x17%\x96\xdat|\x8c'
iv_c = b'\xe8O\x87&\x16\xdbf\xca\xfa\xa1\xf7\xe4\xc2\x0c\x18\xe2'


HOST = '127.0.0.1'#'ec2-18-220-181-73.us-east-2.compute.amazonaws.com'
HOST1 = '127.0.0.1'
PORT = 8080
PORT1 = 8010

#listening and accepting connection from client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind((HOST,PORT))
#s.listen(5)
#c,addr = s.accept()
#print('connected to client',HOST)

#listening and accepting connection from client1:
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((HOST1,PORT1))
s1.listen(5)
#c1,addr1 = s1.accept()


def dec_client(data):
    decryptor  = AES.new(key_c,AES.MODE_CBC,iv_c)
    return decryptor.decrypt(data)

def dec_server(data):
    decryptor  = AES.new(key_s,AES.MODE_CBC,iv_s)
    return decryptor.decrypt(data)

def enc(data):
    encryptor = AES.new(key_c,AES.MODE_CBC,iv_c)
    return encryptor.encrypt(data)
s.connect((HOST,PORT))
cc = None
#while True:
if cc is None:
    cc,addr = s1.accept()
#print('ha')
#encrypted id received:
data = cc.recv(1024)
id = dec_client(data)
#id = id.decode('utf-8')
#print(id)
#send to server:

s.sendall(id)
#print('sent')
#receive file:
data = s.recv(2048)
data = dec_server(data)
#print(data)
#with open('file.txt','wb') as f:
    #f.write(enc(data))
cc.send(enc(data))
#print('hahahahahah')
cc.close()
s.close()
    




