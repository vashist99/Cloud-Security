
import os

file_name = 'data/file_10kB'
one_kb = 1024  # size in bytes
for i in range(60):
    # if i<10:
    #     file = file_name+"0"+str(i)
    # else:
    file = file_name+(str(i))
    #print(file)
    with open(file, "wb") as f:
        f.write(os.urandom(10 * one_kb))