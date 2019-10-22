import socket, os
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RSAImplementation
import time
from Crypto.Cipher import AES
import math


key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'
encryptor = AES.new(key, AES.MODE_CBC, iv)

file_name = 'file_1kb_'
one_kb = 1024
for i in range(60):
	file = 'Data/' + file_name + (str(i))
	#print(file)
	with open(file, "wb") as f:
		data = os.urandom(10*one_kb)
		enc_data = encryptor.encrypt(data)
		f.write(enc_data)