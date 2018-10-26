#!/usr/bin/python

fileName = {'Course':'Python', 'type' : 'Programming', 'boolean': 1}

sample = {1: "one", 2 : "two"}
"""
print (fileName.get('type'))

# print (fileName.has_key('Programming')) # AttributeError: 'dict' object has no attribute 'has_key'

print (fileName.items())

print(fileName)

#reset the dictionary
print(sample)
print (sample.clear())
print (sample)

#getting all key and values
print (fileName.keys())
print (fileName.values())

#coping a dictionary
newFile = fileName.copy()
print (newFile)
"""
#Setting a new dictionary with existing keys

account = ('name', 'address', 'paypal')

abc = dict.fromkeys(account)

print (abc)

#Update the existing dictionary with ("java": "jar")

