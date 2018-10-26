#!/usr/bin/python

'''Python program to check if the input number is odd or even.
A number is even if division by 2 give a remainder of 0.
If remainder is 1, it is odd number.'''

num = int(input("Enter a number: "))
mod = num % 2.
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# or

# print("Even" if int(input()) % 2 == 0 else "Odd")
