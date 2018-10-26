#!/usr/bin/python

# setdefault()

var1 = {'Name': 'minnu', 'Age': 7}

print ("Value : %s" %  var1.setdefault('Age', None))

print ("Value : %s" %  var1.setdefault('course', 'PyBuilder'))
