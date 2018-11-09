#!/usr/bin/python


for a in range(1,16):  # end-1 16-1 =15
    if(a in range(9,14)):  # end-1 14-1=13
        print(a, "is matching")
        continue
    else:
        print(a)

print("I am outside of for loop")
"""
for i in range(1,16):
    print(i)
"""
