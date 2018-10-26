#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']: ", dict['Class'])

del dict['Name']; # remove entry with key 'Name'

print ("dict['Age']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Age']: ", dict['Class'])

dict.clear();     # remove all entries in dict

del dict ;        # delete entire dictionary

print ("dict['Age']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Age']: ", dict['Class'])
print ("dict['School']: ", dict['School'])
