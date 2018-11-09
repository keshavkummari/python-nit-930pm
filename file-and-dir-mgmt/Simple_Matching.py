# Simple Matching :

import fnmatch
import os

#pattern = 'fnmatch_*.py'
pattern = 'Reading*.py'
print('Pattern :', pattern)
print("")

files = os.listdir('.')
for name in files:
    print('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern)))