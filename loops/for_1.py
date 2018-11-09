#!/usr/bin/python

count=0

name=input("Enter your name to find out no of Vowels: ")


for a in name:
    print(a)

for a in name:
    if (a in ["A","E","I","O","U","a","e","i","o","u"]):
        count = count + 1

print ("You have", count, "Vowels in your name")
