#!/usr/bin/python

import os
from fnmatch import fnmatch

root = '/samba-test/'
extension = "*.csv"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, extension):
            print (os.path.join(path, name))
            
