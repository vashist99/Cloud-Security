import socket, os
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RSAImplementation
import time
from Crypto.Cipher import AES
import math
#from Crypto.Hash import SHA512


def encrypt_file(key, in_filename, iv):
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    with open(in_filename, "rb") as infile:
        plaintext = infile.read()
        ciphertext = encryptor.encrypt(plaintext)
        return ciphertext



key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'
def main():
    # connecting to server
    HOST = '127.0.0.1'
    PORT = 11113
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    c, addr = s.accept()
    print("connected to client")
   
    
    while True:
        a1 = c.recv(1024) # receiving request
        if a1 == b'':
            c, addr = s.accept()
            print("connected to client")
        if a1 != b'':
            a = int(a1)
            filename = "file_10kb"
            cur_path = os.path.dirname(__file__)
            #for i in range(len(a)):
            if(int(a)<10):
                in_filename = filename+"0"+str(int(a))
            else:
                in_filename = filename+str(int(a))
    
            # encrypting file
            enc_data = encrypt_file(key,in_filename, iv)
            f2 = open("enc_file.txt", "wb")
            f2.write(enc_data)
            f2.close()
            print("file encrypted")

            # sending file to server:
            f2 = open("enc_file.txt", "rb")
            c.sendfile(f2)
            print("encrypted file sent")
            f2.close()
            #c.close()

    print('done')   

if __name__ == "__main__":
    main()
