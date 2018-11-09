#!/usr/bin/python
count=0
name=input("Enter your name to find out no of Consonants : ")

for letter in name:
    if (letter in ['B','b','C','c','D','d','F','f','G','g','H','h','J','j','K','k','L','l','M','m','N','n','P','p',
'Q','q','R','r','S','s','T','t','V','v','W','w','X','x','Y','y','Z','z']):
        count=count+1
print ("Your name contains",count,"Consonants in your name")

