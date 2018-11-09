#!/usr/bin/python

try:
   f = open("C:/Users/Jessicah Princess/Desktop/sample.txt",encoding = 'utf-8')
   print(f.read())
   # perform file operations
finally:
   f.close()

print ("'''*********************************************************'''")
"""
with open("C:/Users/Jessicah Princess/Desktop/test.txt",encoding = 'utf-8') as f:
    print (f.read())
   # perform file operations


# Script mode:

with open("test.txt",'a',encoding = 'utf-8') as f:
   f.write("LINUX\n")
   f.write("UNIX\n\n")
   f.write("PERL-UNIX\n")
"""
'w'		Open a file for writing. Creates a new file if it does not 
		exist or truncates the file if it exists.   """
"""
with open("test.txt") as abc:
    print(abc.read())
    
"""
""""
