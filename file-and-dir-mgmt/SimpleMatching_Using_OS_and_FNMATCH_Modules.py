#!/usr/bin/python
# Simple Matching :
                                         
import fnmatch
import os

#pattern = 'fnmatch_*.py'
pattern = 'fnmatch_.py'

print ('Pattern :', pattern)
print ("")

files = os.listdir('.')
#files = os.listdir('C:\\Users\\Jessicah Princess\\Desktop\\')
for name in files:
    print ('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern)))
