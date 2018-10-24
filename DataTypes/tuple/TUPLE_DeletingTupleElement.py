#!/usr/bin/python

tup = ('python', 'linux', 1997, 2000)

print (tup)

del tup
#del tup[0]  # TypeError: 'tuple' object doesn't support item deletion

print ("After deleting tup : ")

print (tup)   # NameError: name 'tup' is not defined
