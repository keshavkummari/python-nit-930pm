#!/usr/bin/python
import random 
print ("Random number with seed 10 : ", random.random())
random.seed(0)
print ("Random number with seed 10 : ", random.random())

# It will generate same random number
#random.seed( 3 )
print ("Random number with seed 10 : ", random.random())

# It will generate same random number
#random.seed( 2 )
#print ("Random number with seed 10 : ", random.random())
