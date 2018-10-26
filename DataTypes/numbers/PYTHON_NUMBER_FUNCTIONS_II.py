# Random Number Functions :

'''
Random numbers are used for
games,
simulations,
testing,
security, and
privacy applications.'''

'''************************************************************
Function	Description
---------------------------------------------------------------
1. choice(seq)	        A random item from a list, tuple, or string.
2. randrange
([start,] stop [,step])	A randomly selected element from range(start, stop, step)
3. random()	        A random float r, such that 0 is less than or equal to r and r is less than 1
4. seed([x])	        Sets the integer starting value used in generating
                        random numbers.
                        Call this function before calling any other
                        random module function.Returns None.
                        
5. shuffle(lst)	        Randomizes the items of a list in place. Returns None.
6. uniform(x, y)	A random float r, such that x is less than or equal to r
                        and r is less than y

************************************************************'''

# 1. choice() Method :
The method choice() returns a random item from a list, tuple, or string.

Syntax: choice( seq )
seq -- This could be a list, tuple, or string...

#!/usr/bin/python
import random # module

print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('Redhat Centos Ubuntu') : ", random.choice('Redhat Centos Ubuntu')

'''************************************************************'''
2. randrange() Method :

The method randrange() returns a randomly selected element from range(start, stop, step).

Syntax :
randrange ([start,] stop [,step])

start -- Start point of the range. This would be included in the range. .

stop -- Stop point of the range. This would be excluded from the range..

step -- Steps to be added in a number to decide a random number..

#!/usr/bin/python
import random

# Select an even number in 100 <= number < 1000
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# Select another number in 100 <= number < 1000
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)

'''************************************************************'''
3. random() Method :

The method random() returnsa random float r,
such that 0 is less than or equal to r and r is less than 1.

Syntax : random ( )

#!/usr/bin/python
import random

# First random number
print "random() : ", random.random()

# Second random number
print "random() : ", random.random()
'''************************************************************'''
4. seed() Method :

The method seed() sets the integer starting value used in generating random numbers.
Call this function before calling any other random module function.

Syntx : seed ( [x] )

x : This is the seed for the next random number.
If omitted, then it takes system time to generate next random number.

#!/usr/bin/python
import random

random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()
'''************************************************************'''
5. shuffle() Method :

The method shuffle() randomizes the items of a list in place.

Syntax : shuffle (lst )

lst -- This could be a list or tuple.

#!/usr/bin/python
import random

list = [20, 16, 10, 5];
random.shuffle(list)
print "Reshuffled list : ",  list

random.shuffle(list)
print "Reshuffled list : ",  list
'''************************************************************'''
6. uniform() Method :

The method uniform() returns a random float r,
such that x is less than or equal to r and r is less than y.

Syntax : uniform(x, y)

x -- Sets the lower limit of the random float.
y -- Sets the upper limit of the random float.


#!/usr/bin/python
import random

print "Random Float uniform(5, 10) : ",  random.uniform(5, 10)

print "Random Float uniform(7, 14) : ",  random.uniform(7, 14)

'''************************************************************'''
# Trigonometric Functions :

Function :
1. acos(x)
2. asin(x)
3. atan(x)
4. atan2(y, x)
5. cos(x)
6. hypot(x, y)
7. sin(x)
8. tan(x)
9. degrees(x)
10. radians(x)   
'''************************************************************'''
1. acos() Method :

The method acos() returns the arc cosine of x, in radians.

x -- This must be a numeric value in the range -1 to 1.
If x is greater than 1 then it will generate an error.


#!/usr/bin/python
import math

print "acos(0.64) : ",  math.acos(0.64)
print "acos(0) : ",  math.acos(0)
print "acos(-1) : ",  math.acos(-1)
print "acos(1) : ",  math.acos(1)


'''************************************************************'''
2. asin() Method :

The method asin() returns the arc sine of x, in radians.

Syntax: asin(x)

x -- This must be a numeric value in the range -1 to 1.
If x is greater than 1 then it will generate an error.

#!/usr/bin/python
import math

print "asin(0.64) : ",  math.asin(0.64)
print "asin(0) : ",  math.asin(0)
print "asin(-1) : ",  math.asin(-1)
print "asin(1) : ",  math.asin(1)

'''************************************************************'''
3. atan() Method :

The method atan() returns the arc tangent of x, in radians.

Syntax : atan(x)

x -- This must be a numeric value.

#!/usr/bin/python
import math

print "atan(0.64) : ",  math.atan(0.64)
print "atan(0) : ",  math.atan(0)
print "atan(10) : ",  math.atan(10)
print "atan(-1) : ",  math.atan(-1)
print "atan(1) : ",  math.atan(1)
'''************************************************************'''
4. atan2() Method :

The method atan2() returns atan(y / x), in radians.

Syntax : atan2(y, x)

y -- This must be a numeric value.

x -- This must be a numeric value.

#!/usr/bin/python
import math

print "atan2(-0.50,-0.50) : ",  math.atan2(-0.50,-0.50)
print "atan2(0.50,0.50) : ",  math.atan2(0.50,0.50)
print "atan2(5,5) : ",  math.atan2(5,5)
print "atan2(-10,10) : ",  math.atan2(-10,10)
print "atan2(10,20) : ",  math.atan2(10,20)
'''************************************************************'''
5. cos() Method:

The method cos() returns the cosine of x radians.

Syntax : cos(x)

x -- This must be a numeric value.

#!/usr/bin/python
import math

print "cos(3) : ",  math.cos(3)
print "cos(-3) : ",  math.cos(-3)
print "cos(0) : ",  math.cos(0)
print "cos(math.pi) : ",  math.cos(math.pi)
print "cos(2*math.pi) : ",  math.cos(2*math.pi)

Output: 
This method returns a numeric value between -1 and 1,
which represents the cosine of the angle.

'''************************************************************'''
6. hypot() Method :

The method hypot() return the Euclidean norm, sqrt(x*x + y*y).

Syntax : hypot(x, y)

x -- This must be a numeric value.

y -- This must be a numeric value

#!/usr/bin/python
import math

print "hypot(3, 2) : ",  math.hypot(3, 2)
print "hypot(-3, 3) : ",  math.hypot(-3, 3)
print "hypot(0, 2) : ",  math.hypot(0, 2)
    
'''************************************************************'''
7. sin() Method :

The method sin() returns the sine of x, in radians.

Syntax : sin(x)

x : This must be a numeric value.

#!/usr/bin/python
import math

print "sin(3) : ",  math.sin(3)
print "sin(-3) : ",  math.sin(-3)
print "sin(0) : ",  math.sin(0)
print "sin(math.pi) : ",  math.sin(math.pi)
print "sin(math.pi/2) : ",  math.sin(math.pi/2)

Output:
This method returns a numeric value between -1 and 1,
which represents the sine of the parameter x.

'''************************************************************'''
8. tan() Method :

The method tan() returns the tangent of x radians.
This method returns a numeric value between -1 and 1,
which represents the tangent of the parameter x.

Syntax : tan(x)
x -- This must be a numeric value.

#!/usr/bin/python
import math

print "tan(3) : ",  math.tan(3)
print "tan(-3) : ",  math.tan(-3)
print "tan(0) : ",  math.tan(0)
print "tan(math.pi) : ",  math.tan(math.pi)
print "tan(math.pi/2) : ",  math.tan(math.pi/2)
print "tan(math.pi/4) : ",  math.tan(math.pi/4)    
'''************************************************************'''
9. degrees() Method :

The method degrees() converts angle x from radians to degrees..
This method returns degree value of an angle.

Syntax : degrees(x)
x -- This must be a numeric value.

#!/usr/bin/python
import math

print "degrees(3) : ",  math.degrees(3)
print "degrees(-3) : ",  math.degrees(-3)
print "degrees(0) : ",  math.degrees(0)
print "degrees(math.pi) : ",  math.degrees(math.pi)
print "degrees(math.pi/2) : ",  math.degrees(math.pi/2)
print "degrees(math.pi/4) : ",  math.degrees(math.pi/4)    
'''************************************************************'''
10. radians() Method :

The method radians() converts angle x from degrees to radians.
This method returns radian value of an angle.

Syntax : radians(x)

x -- This must be a numeric value.

#!/usr/bin/python
import math

print "radians(3) : ",  math.radians(3)
print "radians(-3) : ",  math.radians(-3)
print "radians(0) : ",  math.radians(0)
print "radians(math.pi) : ",  math.radians(math.pi)
print "radians(math.pi/2) : ",  math.radians(math.pi/2)
print "radians(math.pi/4) : ",  math.radians(math.pi/4)    
'''************************************************************'''
# Mathematical Constants :
    
The module also defines two mathematical constants:

Constants	Description
pi	        The mathematical constant pi.
e	        The mathematical constant e.

math.pi
The mathematical constant π = 3.141592..., to available precision.

math.e
The mathematical constant e = 2.718281..., to available precision.

'''************************************************************'''


    


