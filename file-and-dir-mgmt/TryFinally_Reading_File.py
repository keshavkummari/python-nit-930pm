#!/usr/bin/python
import os

try:
   f = open("/Users/keshavkummari/Desktop/abc.txt",encoding = 'utf-8')

   # perform file operations
   print(f.read())
   print("Current Cursor Position : ",f.tell())
   print("Bring the Cursor to 0th index: ",f.seek(0))
   print("Current Cursor Position : ",f.tell())
   print(f.readline())
   print("Current Cursor Position : ",f.tell())
   print(f.readlines())
   print("Current Cursor Position : ",f.tell())

finally:
   f.close()
