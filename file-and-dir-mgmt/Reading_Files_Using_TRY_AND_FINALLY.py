#!/usr/bin/python

try:
   f = open("C:/Users/Jessicah Princess/Desktop/test.txt",encoding = 'utf-8')
   print(f.read())
   # perform file operations
finally:
   f.close()

print ("'''*********************************************************'''")
