import socket
from Crypto.Cipher import AES
import random
import time
import sys
#from os import stat,remove

rint = random.randint
key = b'[\xfb?\t\xd1#|\xdeQ\x17%\x96\xdat|\x8c'
iv = b'\xe8O\x87&\x16\xdbf\xca\xfa\xa1\xf7\xe4\xc2\x0c\x18\xe2'



#connecting to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 8006
#

bs = AES.block_size
pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
def dec(data):
    decryptor = AES.new(key,AES.MODE_CBC,iv)
    return decryptor.decrypt(data)

def enc(data):
    data = pad(data)
    data = data.encode('utf-8')
    encryptor = AES.new(key,AES.MODE_CBC,iv)
    return encryptor.encrypt(data)


s.connect((HOST,PORT))
#print('ADW')
s.sendall(enc(str(rint(0,60))))
#print('hello')
# with open('final.txt','wb') as f:
#     f.write()

d = s.recv(2048)
d = dec(d)
#print(d)
with open('final.txt','wb') as po:
    po.write(d)
    #print('received')


s.shutdown(socket.SHUT_RDWR)
s.close()
po.close()
sys.exit()


