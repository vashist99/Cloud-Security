import socket
import time
import random
from Crypto.Hash import SHA512
from Crypto.Cipher import AES


# generating key obj
rint = random.randint

key = b'\x8a\x04Va{\x11\xfc\xdeW\x12\xbc/\xed\x10\x0f\x16\x14a\xadv\xc0\n\x889\xe4\x0c\xc82\x8f\xbe\x1cp'
iv = b'Vs0\xb5\x0e\xfdr\x05\xf4\x84\x93\xe4\x95\x041\xa4'


def decrypt_file(key, data, iv):
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = data
    plaintext = decryptor.decrypt(ciphertext)
    return plaintext


def main():
    # listening and accepting connection from client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 11113
    s.connect((HOST, PORT))
    print("connected to server")

    print("chose the file size to be transfered: 10kB 100kB 1MB 100MB ")
    sze = str(input())
    if(sze=="10kB"):
        filename = "file_10kb"       
    elif sze=="100kB":
        filename = "file_100kb"
    elif sze=="1MB":
        filename = "file_1Mb"
    elif sze=="10MB":
        filename = "file_10MB"

    num = int(input("Chose the number of files"))
    sum=0
    for j in range(20):
        for i in range(num):
            start = time.time()
            temp = rint(1,59)
            temp1 = str(temp).encode('utf-8')
            # sending id:
            s.send(temp1)
            # recieving encrypted file from client
            enc_data = s.recv(10000000)

            ptext = decrypt_file(key,enc_data,iv)
            #filename = 'file_10kb'
            if temp<10:
                in_filename = filename+"0"+str(temp)
            else:
                in_filename = filename+str(temp)
            f = open(in_filename,'wb')
            f.write(ptext)
            f.close()       
        end_time = time.time()
        sum+=(end_time-start)
    print(sum/20)
    #s.close()


if __name__ == "__main__":
    main()
