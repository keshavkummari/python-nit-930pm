#!/usr/bin/python

import os
from fnmatch import fnmatch

#root = 'C:\\Users\\Jessicah Princess\\Desktop\\'

root = '/Users/keshavkummari/KK/_PYTHON/8_File_and_Direct_Mgmt/'

extension = "*.txt"

for path, subdirs, files in os.walk(root): 
    for name in files:
        if fnmatch(name, extension):
            print (os.path.join(path, name))
