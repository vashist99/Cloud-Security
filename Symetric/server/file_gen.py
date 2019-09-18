
import os

file_name = 'file_1Mb'
one_kb = 1024  # size in bytes
for i in range(60):
    if i<10:
        file = file_name+"0"+str(i)
    else:
        file = file_name+(str(i))
    #print(file)
    with open(file, "wb") as f:
        f.write(os.urandom(one_kb * one_kb))