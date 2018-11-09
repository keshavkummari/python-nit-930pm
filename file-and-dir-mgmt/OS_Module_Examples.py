#!/usr/bin/python

# Import a Module i.e. Operating Systems(os)

import os

print(os.getcwd())

print(os.chdir("/Users/keshavkummari"))

print(os.getcwd())

print(os.listdir())

print(os.chdir("python-nit-930pm"))

print(os.getcwd())

print(os.listdir())

#print(os.mkdir("file-and-dir-mgmt"))

print(os.listdir())

path="/Users/keshavkummari/python-nit-930pm/file-and-dir-mgmt/"

print(os.chdir(path))

print(os.getcwd())

print(os.listdir())

#file = open("info.txt","w")

#file.write("Welcome to Python World by Keshav Kummari\n")
#file.write("Python on AWS\n")
#file.write("Python on AZURE\n")
#file.write("Automate Infrastructure using Python\n")

print(os.listdir())

f = open("info.txt","r")
print(f.readline())    # Read only one line
print(f.readlines())   # Read remaining lines
print(f.tell())        # Current Cursor Position
print(f.seek(0))       # Bring the cursor to specific location
print(f.read())        # Read entire file
f.close()              # Close the file