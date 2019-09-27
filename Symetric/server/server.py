import socket, os
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RSAImplementation
import time
from Crypto.Cipher import AES
import math


key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'
encryptor = AES.new(key, AES.MODE_CBC, iv)

FILE_NAME_BASE = "file_1kb_"

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
	conn, addr = s.accept()
	start = time.time()
	ids = conn.recv(1024).decode("utf-8")
	for id in ids.split(','):
		with open('./Data/' + FILE_NAME_BASE + id, 'rb') as infile:
			conn.sendfile(infile)
	end = time.time()
	conn.close()
	print(start)
	print(end)
	print(end-start)