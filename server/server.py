import socket
from Crypto.Cipher import AES
import time

#assigning key:
key = b'T\x91\x86\xe6\xa3\x19\xb4\x10~\xc3\xe9\xcf\t\xa3\xec\xd8'
iv = b'A]L\x93\xb4\xae\xbc\xd7\xa0\xf4\xa9\xd7\xee2Y\x0c'

#connecting to server:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 8006
s.bind((HOST,PORT))
s.listen(5)

def enc(data):
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    return encryptor.encrypt(data)
    

c,addr = s.accept()
#while True:
#print('he')
#recieving id:
id = c.recv(1024)
id = id.decode('utf-8')
#print('rec')

with open('./Data/file_1kb_'+'12','rb') as f:
    data = f.read()
    #enc_data = enc(data)
    #f2.write(enc_data)
    c.sendall(enc_data)
    #print('sent')
    f.close()






