import socket, os
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RSAImplementation
import time
from Crypto.Cipher import AES
import math
#from Crypto.Hash import SHA512


def encrypt_file(key, in_filename, iv):
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    with open('data/' + in_filename, "rb") as infile:
        plaintext = infile.read()
        ciphertext = encryptor.encrypt(plaintext)
        return ciphertext



key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'
FILE_SIZE = '10kB'
def main():
    # connecting to server
    HOST = '127.0.0.1'
    PORT = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    # c, addr = s.accept()
    #print("connected to client")
    while True:
        start = time.time()
        c, addr = s.accept()
        a1 = c.recv(1024) # receiving request
        a2 = a1.decode('utf-8')
        for a in a2.split(','):
            in_filename = 'file_'+FILE_SIZE + a
            enc_data = encrypt_file(key,in_filename, iv)
            c.send(enc_data)
        end = time.time()
        print(start)
        print(end)
        print(end - start)
        c.close()

    #print('done')   

if __name__ == "__main__":
    main()
