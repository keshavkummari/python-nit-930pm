#!/usr/bin/python
import math   # This will import math module

'''11. modf(x) : The fractional and integer parts of x in a two-item tuple. 
Both parts have the same sign as x. 
The integer part is returned as a float.'''

#Python modf() Method:
print "math.modf(100.12) : ", math.modf(100.12)
print "math.modf(100.72) : ", math.modf(100.72)
print "math.modf(119L) : ", math.modf(119L)
print "math.modf(math.pi) : ", math.modf(math.pi)

#modf() 
print "modf method", math.modf(22.67)
