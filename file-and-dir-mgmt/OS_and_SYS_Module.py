#!/usr/bin/python
import os, sys

if sys.platform == 'win32':
     print ("Running on a windows platform")
     command = "C:\\winnt\\system32\\cmd.exe"
     params = []
     print("Running %s" % (command))

if sys.platform == 'linux2':
     print ("Running on a Linux system, identified by %s" % sys.platform)
     command = '/bin/uname'
     params = ['uname', '-a']
     print("Running %s" % (command))

if sys.platform == 'darwin':
     print ("Running on a MacOS system, identified by %s" % sys.platform)
     command = '/usr/bin/uname'
     params = ['uname', '-a']
     print ("Running %s" %(command))

#os.spawnv(os.P_WAIT, command, params)
