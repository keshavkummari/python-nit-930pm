#!/usr/bin/python

'''cat file_modes_write_and_read.py'''

'''
modes to open file :
r, rb, r+, rb+, w, wb, w+, wb+, a, ab, a+, ab+
'''
#Writing a file

fileObject = open("C:\\Users\\Jessicah Princess\\Desktop\\sample.txt", "wb+")
fileObject.write("This is testing of python")
print(fileObject)
fileObject.write("This line is by Deepthi")
print(fileObject)
fileObject.write("This is by Avinash")
print(fileObject)
fileObject.close()

#Reading a file

fileObjectNew = open("sample.txt", "r+")
fileText = fileObjectNew.read(200)
print (fileText)
fileObjectNew.close()
