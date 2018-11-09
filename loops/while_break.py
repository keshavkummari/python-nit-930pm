#!/usr/bin/python

redhat=1

while (redhat<10):# True condition and it will execute until false condition encounters
    print ("Hi I am while loop",redhat, sep="::")
    if redhat == 5:
        print("Condition is met", redhat == 5)
        break
    else:
        print("I am executing else block")
        redhat=redhat+1

print ("")
print ("We are out of the while block")  

