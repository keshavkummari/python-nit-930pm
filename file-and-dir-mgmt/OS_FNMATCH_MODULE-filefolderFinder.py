#!/usr/bin/python

import os
from fnmatch import fnmatch

root = 'C:/Users/Jessicah Princess/Desktop'
extension = "*.py"

for path, subdirs, files in os.walk(root): 
    for name in files:
        if fnmatch(name, extension):
            print (os.path.join(path, name))
            
            
