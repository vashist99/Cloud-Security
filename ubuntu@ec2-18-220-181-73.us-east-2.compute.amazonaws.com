import socket
import time
import random
from Crypto.Hash import SHA512
from Crypto.Cipher import AES

rint = random.randint

key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'
decryptor = AES.new(key, AES.MODE_CBC, iv)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 11113

FILE_NAME_BASE = 'file_1kb_'
ONE_KB = 1024
FILE_SIZE = ONE_KB

num = int(input("Chose the number of files: "))
ids = [str(rint(1,59)) for x in range(num)]
data = ','.join(ids)

start = time.time()
s.connect((HOST, PORT))
s.send(str.encode(data))

for i in range(num):
	enc_data = s.recv(FILE_SIZE)
	dec_data = decryptor.decrypt(enc_data)
	with open('./Received/' + FILE_NAME_BASE + str(i), 'wb') as outfile:
		outfile.write(dec_data)

s.close()
end = time.time()

print(start)
print(end)
print(end-start)