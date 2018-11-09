# OS.Walk and Fnmatch in Python :

# What is OS.walk?

It generates the file names in a directory tree by walking the tree either
top-down or bottom-up.

For each directory in the tree rooted at directory top (including top itself), 
it yields a 3-tuple (dirpath, dirnames, filenames).

1. dirpath	# is a string, the path to the directory. 

2. dirnames	# is a list of the names of the subdirectories in dirpath
		  (excluding '.' and '..'). 

3. filenames	# is a list of the names of the non-directory files in dirpath. 

# Note that the names in the lists contain no path components.

# What is Fnmatch :

The fnmatch module compares file names against glob-style patterns such as used
by Unix/Linux shells.

These are not the same as the more sophisticated regular expression rules. 

Its purely a string matching operation. 

If you find it more convenient to use a different pattern style, for example 
regular expressions, then simply use regex operations to match your filenames.

"""****************************************************"""
# What does it do?

The fnmatch module is used for the wild-card pattern matching.

# Simple Matching
fnmatch() compares a single file name against a pattern and
returns a boolean indicating whether or not they match. 

The comparison is case-sensitive when the operating system uses a case-sensitive
file system.

# Filtering
To test a sequence of filenames, you can use filter(). 

It returns a list of the names that match the pattern argument.

"""****************************************************"""
# Find all mp3 files
# This script will search for *.mp3 files from the rootPath ("/")

import fnmatch
import os
 
rootPath = '/'
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
"""****************************************************"""
# Search computer for specific files :

"""This script uses 'os.walk' and 'fnmatch' with filters to search the hard-drive
for all image files"""

import fnmatch
import os

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk("C:\"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))

"""****************************************************"""
# Simple Matching :
                                         
import fnmatch
import os

pattern = 'fnmatch_*.py'
print ('Pattern :', pattern)
print ("")

files = os.listdir('.')
for name in files:
    print ('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern)))
"""****************************************************"""
To force a case-sensitive comparison, regardless of the filesystem and
operating system settings, use fnmatchcase().

import fnmatch
import os

pattern = 'FNMATCH_*.PY'
print 'Pattern :', pattern
print

files = os.listdir('.')

for name in files:
    print 'Filename: %-25s %s' % (name, fnmatch.fnmatchcase(name, pattern))
"""****************************************************"""
Filtering

To test a sequence of filenames, you can use filter(). It returns a list of the names that match the pattern argument.

import fnmatch
import os

pattern = 'fnmatch_*.py'
print 'Pattern :', pattern

files = os.listdir('.')
print 'Files   :', files

print 'Matches :', fnmatch.filter(files, pattern)
In this example, filter() returns the list of names of the example source files associated with this post.
"""****************************************************"""
Translating Patterns

Internally, fnmatch converts the glob pattern to a regular expression and uses the re module to compare the name and pattern. The translate() function is the public API for converting glob patterns to regular expressions.

import fnmatch

pattern = 'fnmatch_*.py'
print 'Pattern :', pattern
print 'Regex   :', fnmatch.translate(pattern)
Notice that some of the characters are escaped to make a valid expression.
"""****************************************************"""                                         

