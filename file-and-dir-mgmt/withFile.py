#!/usr/bin/python
import os

#os.chdir("C:\\Users\\Jessicah Princess\\Desktop")

os.chdir("/Users/keshavkummari/KK/_PYTHON/8_File_and_Direct_Mgmt/")

with open("sample.txt")as file:
    print(file.read())
    print("BringTheCursorTo0thIndex : ", file.seek(0))
    print(file.readline())
    print(file.readlines())
    #file.close()  # No need of using file.close() with "with" statement

#with open("sample.txt",'w',encoding = 'cp1252') as f:
"""
with open("sample.txt",'w') as f:
   f.write("Mac\n")
   f.write("iphone7\n\n")
   f.write("contains three lines\n")
      
with open("sample.txt")as a:
    print(a.read())
    print(a.readline())
    print(a.readlines())
    

# Open a file
fo = open("sample.txt", "r+")
str = fo.read();
print ("Read String is : ", str)
# Close opend file
fo.close()
print("Another prog")
str = input("Enter your input: ");
print ("Received input is : ", str)
"""
