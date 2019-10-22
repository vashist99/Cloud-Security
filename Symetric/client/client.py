import socket
import time
import random
from Crypto.Hash import SHA512
from Crypto.Cipher import AES

rint = random.randint

def recv_basic(the_socket):
    total_data=[]
    while True:
        data = the_socket.recv(8192)
        if not data: break
        total_data.append(data)
    return b''.join(total_data)


key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'
decryptor = AES.new(key, AES.MODE_CBC, iv)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "ec2-18-220-181-73.us-east-2.compute.amazonaws.com"
PORT = 8000

FILE_NAME_BASE = 'file_1kb_'
ONE_KB = 1024*1024
FILE_SIZE = ONE_KB

num = int(input("Chose the number of files: "))
ids = [str(rint(1,59)) for x in range(num)]
data = ','.join(ids)

start = time.time()
s.connect((HOST, PORT))
s.send(str.encode(data))

for i in range(num):
	enc_data = recv_basic(s)
	dec_data = decryptor.decrypt(enc_data)
	with open('./Received/' + FILE_NAME_BASE + str(i), 'wb') as outfile:
		outfile.write(dec_data)

s.close()
end = time.time()

print(start)
print(end)
print(end-start)
