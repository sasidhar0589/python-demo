# "r" -> reading a file
# "w" -> writing a file
# "a" -> appending a file
#x -> creating a file 
# "t" -> we have text data 
# "b" -> we have binary data( images, videos, audio files)
#r+ -> read and write
#w+ -> write and read
# Compare this snippet from python-demo/python_file_handling.py
# -> open() we can open a file 
# -> read() we can read a file but we need to open it first
# -> close() we can close a file
import os
path = os.getcwd()
# path = os.path.dirname(path).join("/file_handeling/")
path = path+"/file_handeling/"
print(path)

# f = open(path+"temp_file_read.txt") # open() at least path to open the file 
# f.close()
f = open(path+"temp_file_read.txt","rt") # open
for file_line in f:
    print(file_line)



# f2 = open(path+"temp_file_write.txt","x") # open
f2 = open(path+"temp_file_write.txt","r") # opn
# print(f2.read())
f2.close()
f2 = open(path+"temp_file_write.txt","w+")
f2.write("Hello Surya")
# print(f2.read())
f2.close()
f2 = open(path+"temp_file_write.txt","r")
# print(f2.read())
f2.close()
f3 = open(path+"temp_file_write.txt","a")
f3.write("\nHello Swetha")

f3.close()
f3 = open(path+"temp_file_write.txt","r")
f2.close()
# print(f3.read())

# remove a file 

with open(path+"temp_file_write.txt","r+") as f4:
    print(f4.read())
    f4.write("\nHello Sasi")
    f4.seek(0)
    print(f4.read())
    f4.close()