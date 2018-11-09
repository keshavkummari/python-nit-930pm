#!/usr/bin/python

with open("C:/Users/Jessicah Princess/Desktop/sample.txt")as file:
    print(file.read())
    print(file.readlines())
    file.close()

with open("Airtel.txt",'w',encoding = 'utf-8') as f:
   f.write("Mac\n")
   f.write("iphone7\n\n")
   f.write("contains three lines\n")
   f.close()

with open("C:/Users/Jessicah Princess/Desktop/sample.txt") as f:
     print(f.read())

# Open a file
fo = open("Airtel.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

# Open a file
fo = open("test.txt", "r+")
str = fo.read(1);
print ("Read String is : ", str)
# Close opend file
fo.close()


print("Another prog")

str = input("Enter your input: ");
print ("Received input is : ", str)
