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
    HOST = '127.0.0.1'
    #"ec2-18-220-181-73.us-east-2.compute.amazonaws.com"
    PORT = 12345
    s.connect((HOST, PORT))
    print("connected to server")

    # print("chose the file size to be transfered: 10kB 100kB 1MB 100MB ")
    # sze = str(input())
    # if(sze=="10kB"):
    #     filename = "file_10kB"       
    # elif sze=="100kB":
    #     filename = "file_100kB"
    # elif sze=="1MB":
    #     filename = "file_1MB"
    # elif sze=="10MB":
    #     filename = "file_10MB"

    filename = 'file_10kB'
    num = int(input("Chose the number of files"))
    ids = []
    for i in range(num):
        temp = rint(1,59)
        ids.append(str(temp))
    send_data = ','.join(ids)
    send  = send_data.encode('utf-8')
    start = time.time()
    s.send(send)
    # recieving encrypted file from client
    for i in range(num):
        enc_data = s.recv(1024)
        ptext = decrypt_file(key,enc_data,iv)
        in_filename = 'data/'+filename + str(i)
        with open(in_filename, "wb") as infile:
            infile.write(ptext) 
    end_time = time.time()
    print(start)
    print(end_time)
    print(end_time-start)
    #s.close()


if __name__ == "__main__":
    main()
