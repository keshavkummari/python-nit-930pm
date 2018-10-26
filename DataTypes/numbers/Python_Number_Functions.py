Number data types store numeric values. 

They are immutable data types, means that changing the value of a number data type results in a newly allocated object.

Number objects are created when you assign a value to them. 

For example :
var1 = 1
var2 = 10

You can also delete the reference to a number object by using the del statement. The syntax of the del statement is -

del var1[,var2[,var3[....,varN]]]]
You can delete a single object or multiple objects by using the del statement. For example:

del var
del var_a, var_b

******************************************************

Python supports four different numerical types -

int (signed integers): They are often called just integers or ints, are positive or negative whole numbers with no decimal point.

long (long integers ): Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or lowercase L.

float (floating point real values) : Also called floats, they represent real numbers and are written with a decimal point dividing the integer and fractional parts. Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).

complex (complex numbers) : are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). The real part of the number is a, and the imaginary part is b. Complex numbers are not used much in Python programming.

*********************************************************
Examples
Here are some examples of numbers

int	long		float			complex
10	51924361L	0.0			3.14j
100	-0x19323L	15.20			45.j
-786	0122L		-21.9			9.322e-36j
080	0xDEFABCECBDAECBFBAEL	32.3+e18	.876j
-0490	535633629843L	-90.			-.6545+0J
-0x260	-052318172735L	-32.54e100		3e+26J
0x69	-4721885298529L	70.2-E12		4.53e-7j

Python allows you to use a lowercase L with long, 
but it is recommended that you use only an uppercase L to avoid confusion with the number 1. 
Python displays long integers with an uppercase L.

A complex number consists of an ordered pair of real floating point numbers denoted by a + bj, 
where a is the real part and b is the imaginary part of the complex number.


Number Type Conversion:
***********************
Python converts numbers internally in an expression containing mixed types to a common type for evaluation. But sometimes, you need to coerce a number explicitly from one type to another to satisfy the requirements of an operator or function parameter.

Type int(x) to convert x to a plain integer.

Type long(x) to convert x to a long integer.

Type float(x) to convert x to a floating-point number.

Type complex(x) to convert x to a complex number with real part x and imaginary part zero.

Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions

*****************************************************

Mathematical Functions:

Python includes following functions that perform mathematical calculations.

1. abs(x)  : The absolute value of x: the (positive) distance between x and zero.

Python Number abs() Method:
#!/usr/bin/python
print "abs(-45) : ", abs(-45)
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)

output:
abs(-45) :  45
abs(100.12) :  100.12
abs(119L) :  119

----------------------------------------------------------------
2. ceil(x) : The ceiling of x: the smallest integer not less than x

Python Number ceil() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.ceil(-45.17) : ", math.ceil(-45.17)
print "math.ceil(100.12) : ", math.ceil(100.12)
print "math.ceil(100.72) : ", math.ceil(100.72)
print "math.ceil(119L) : ", math.ceil(119L)
print "math.ceil(math.pi) : ", math.ceil(math.pi)

Output:
math.ceil(-45.17) :  -45.0
math.ceil(100.12) :  101.0
math.ceil(100.72) :  101.0
math.ceil(119L)   :  119.0
math.ceil(math.pi) : 4.0
----------------------------------------------------------------
3. cmp(x, y) : -1 if x < y, 0 if x == y, or 1 if x > y
Python Number cmp() Method:
#!/usr/bin/python
print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)

Output:
cmp(80, 100) :  -1
cmp(180, 100) :  1
cmp(-80, 100) :  -1
cmp(80, -100) :  1
----------------------------------------------------------------
4. exp(x) : The exponential of x: ex

Python Number exp() Method:

#!/usr/bin/python
import math   # This will import math module

print "math.exp(-45.17) : ", math.exp(-45.17)
print "math.exp(100.12) : ", math.exp(100.12)
print "math.exp(100.72) : ", math.exp(100.72)
print "math.exp(119L) : ", math.exp(119L)
print "math.exp(math.pi) : ", math.exp(math.pi)

Output:
math.exp(-45.17) :  2.41500621326e-20
math.exp(100.12) :  3.03084361407e+43
math.exp(100.72) :  5.52255713025e+43
math.exp(119L) :  4.7978133273e+51
math.exp(math.pi) :  23.1406926328
----------------------------------------------------------------
5. fabs(x) : The absolute value of x.
Python Number fabs() Method:

#!/usr/bin/python
import math   # This will import math module

print "math.fabs(-45.17) : ", math.fabs(-45.17)
print "math.fabs(100.12) : ", math.fabs(100.12)
print "math.fabs(100.72) : ", math.fabs(100.72)
print "math.fabs(119L) : ", math.fabs(119L)
print "math.fabs(math.pi) : ", math.fabs(math.pi)

Output:
math.fabs(-45.17) :  45.17
math.fabs(100.12) :  100.12
math.fabs(100.72) :  100.72
math.fabs(119L) :  119.0
math.fabs(math.pi) :  3.14159265359

----------------------------------------------------------------
6. floor(x) : The floor of x: the largest integer not greater than x

Python Number floor() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.floor(-45.17) : ", math.floor(-45.17)
print "math.floor(100.12) : ", math.floor(100.12)
print "math.floor(100.72) : ", math.floor(100.72)
print "math.floor(119L) : ", math.floor(119L)
print "math.floor(math.pi) : ", math.floor(math.pi)

Output:
math.floor(-45.17) :  -46.0
math.floor(100.12) :  100.0
math.floor(100.72) :  100.0
math.floor(119L) :  119.0
math.floor(math.pi) :  3.0
----------------------------------------------------------------
7. log(x) : The natural logarithm of x, for x> 0
Python Number log() Method:
#!/usr/bin/python
import math   # This will import math module
print "math.log(100.12) : ", math.log(100.12)
print "math.log(100.72) : ", math.log(100.72)
print "math.log(119L) : ", math.log(119L)
print "math.log(math.pi) : ", math.log(math.pi)

Output:
math.log(100.12) :  4.60636946656
math.log(100.72) :  4.61234438974
math.log(119L) :  4.77912349311
math.log(math.pi) :  1.14472988585

----------------------------------------------------------------
8. log10(x) : The base-10 logarithm of x for x> 0 .
Python Number log10() Method:
#!/usr/bin/python
import math   # This will import math module
print "math.log10(100.12) : ", math.log10(100.12)
print "math.log10(100.72) : ", math.log10(100.72)
print "math.log10(119L) : ", math.log10(119L)
print "math.log10(math.pi) : ", math.log10(math.pi)

Output:
math.log10(100.12) :  2.00052084094
math.log10(100.72) :  2.0031157171
math.log10(119L) :  2.07554696139
math.log10(math.pi) :  0.497149872694

----------------------------------------------------------------
9. max(x1, x2,...) : The largest of its arguments: the value closest to positive infinity

Python Number max() Method:
#!/usr/bin/python
print "max(80, 100, 1000) : ", max(80, 100, 1000)
print "max(-20, 100, 400) : ", max(-20, 100, 400)
print "max(-80, -20, -10) : ", max(-80, -20, -10)
print "max(0, 100, -400) : ", max(0, 100, -400)

Output:
max(80, 100, 1000) :  1000
max(-20, 100, 400) :  400
max(-80, -20, -10) :  -10
max(0, 100, -400) :  100
----------------------------------------------------------------
10. min(x1, x2,...): The smallest of its arguments: the value closest to negative infinity
Python Number min() Method:
#!/usr/bin/python
print "min(80, 100, 1000) : ", min(80, 100, 1000)
print "min(-20, 100, 400) : ", min(-20, 100, 400)
print "min(-80, -20, -10) : ", min(-80, -20, -10)
print "min(0, 100, -400) : ", min(0, 100, -400)

Output:

min(80, 100, 1000) :  80
min(-20, 100, 400) :  -20
min(-80, -20, -10) :  -80
min(0, 100, -400) :  -400
----------------------------------------------------------------
11. modf(x) : The fractional and integer parts of x in a two-item tuple. 
Both parts have the same sign as x. 
The integer part is returned as a float.

Python modf() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.modf(100.12) : ", math.modf(100.12)
print "math.modf(100.72) : ", math.modf(100.72)
print "math.modf(119L) : ", math.modf(119L)
print "math.modf(math.pi) : ", math.modf(math.pi)

Output:
math.modf(100.12) :  (0.12000000000000455, 100.0)
math.modf(100.72) :  (0.71999999999999886, 100.0)
math.modf(119L) :    (0.0, 119.0)
math.modf(math.pi) :  (0.14159265358979312, 3.0)
----------------------------------------------------------------
12. pow(x, y) : The value of x**y.
Python Number pow() Method:
#!/usr/bin/python
import math   # This will import math module
print "math.pow(100, 2) : ", math.pow(100, 2)
print "math.pow(100, -2) : ", math.pow(100, -2)
print "math.pow(2, 4) : ", math.pow(2, 4)
print "math.pow(3, 0) : ", math.pow(3, 0)

Output:
math.pow(100, 2) :  10000.0
math.pow(100, -2) :  0.0001
math.pow(2, 4) :  16.0
math.pow(3, 0) :  1.0
----------------------------------------------------------------
13. round(x [,n]) : x rounded to n digits from the decimal point. 
Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.

Python Number round() Method:

#!/usr/bin/python

print "round(80.23456, 2) : ", round(80.23456, 2)
print "round(100.000056, 3) : ", round(100.000056, 3)
print "round(-100.000056, 3) : ", round(-100.000056, 3)

Output:
round(80.23456, 2) :  80.23
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
----------------------------------------------------------------
14. sqrt(x) : The square root of x for x > 0

Python Number sqrt() Method:
#!/usr/bin/python
import math   # This will import math module

print "math.sqrt(100) : ", math.sqrt(100)
print "math.sqrt(7) : ", math.sqrt(7)
print "math.sqrt(math.pi) : ", math.sqrt(math.pi)

Output:
math.sqrt(100) :  10.0
math.sqrt(7) :  2.64575131106
math.sqrt(math.pi) :  1.77245385091
----------------------------------------------------------------
Random Number Functions:
Random numbers are used for games, simulations, testing, security, and privacy applications. 

Python includes following functions that are commonly used.

1. choice(seq) : A random item from a list, tuple, or string.

Python Number choice() Method:
#!/usr/bin/python
import random
print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')

Output:
choice([1, 2, 3, 5, 9]) :  2
choice('A String') :  n

----------------------------------------------------------------
2. randrange ([start,] stop [,step]) : 
A randomly selected element from range(start, stop, step)

Python Number randrange() Method:
#!/usr/bin/python
import random

# Select an even number in 100 <= number < 1000
print "randrange(2, 10, 2) : ", random.randrange(2, 10, 2)

# Select another number in 100 <= number < 1000
print "randrange(1, 10, 4) : ", random.randrange(1, 10, 4)

Output:
randrange(100, 1000, 2) :  976
randrange(100, 1000, 3) :  520
----------------------------------------------------------------
3. random(): A random float r, such that 0 is less than or equal to r and r is less than 1

Python Number random() Method:
#!/usr/bin/python
import random

# First random number
print "random() : ", random.random()

# Second random number
print "random() : ", random.random()

Output:
random() :  0.281954791393
random() :  0.309090465205
----------------------------------------------------------------
4. seed([x]) :Sets the integer starting value used in generating random numbers. 
Call this function before calling any other random module function. Returns None.

Python Number seed() Method:
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


Output:
Random number with seed 10 :  0.57140259469
Random number with seed 10 :  0.57140259469
Random number with seed 10 :  0.57140259469
----------------------------------------------------------------
5. shuffle(lst): Randomizes the items of a list in place. Returns None.
Python Number shuffle() Method:
#!/usr/bin/python
import random
list = [20, 16, 10, 5];

random.shuffle(list)
print "Reshuffled list : ",  list

random.shuffle(list)
print "Reshuffled list : ",  list

Output:
Reshuffled list :  [16, 5, 10, 20]
Reshuffled list :  [16, 5, 20, 10]
----------------------------------------------------------------
6. uniform(x, y): A random float r, such that x is less than or equal to r and r is less than y

Python Number uniform() Method:
#!/usr/bin/python
import random

print ("Random Float uniform(5, 10) : "),  random.uniform(5, 10)

print ("Random Float uniform(7, 14) : "),  random.uniform(7, 14)

Output:
Random Float uniform(5, 10) :  5.52615217015
Random Float uniform(7, 14) :  12.5326369199

----------------------------------------------------------------
Trigonometric Functions:

Python includes following functions that perform trigonometric calculations.
1. acos(x) : Return the arc cosine of x, in radians.

Python Number acos() Method:
#!/usr/bin/python
import math

print "acos(0.64) : ",  math.acos(0.64)
print "acos(0) : ",  math.acos(0)
print "acos(-1) : ",  math.acos(-1)
print "acos(1) : ",  math.acos(1)

Output:
acos(0.64) :  0.876298061168
acos(0) :  1.57079632679
acos(-1) :  3.14159265359
acos(1) :  0.0
------------------------------------------------------------
2. asin(x) : Return the arc sine of x, in radians.

Python Number asin() Method:
#!/usr/bin/python
import math

print "asin(0.64) : ",  math.asin(0.64)
print "asin(0) : ",  math.asin(0)
print "asin(-1) : ",  math.asin(-1)
print "asin(1) : ",  math.asin(1)

Output:
asin(0.64) :  0.694498265627
asin(0) :  0.0
asin(-1) :  -1.57079632679
asin(1) :  1.57079632679
------------------------------------------------------------
3. atan(x) : Return the arc tangent of x, in radians.

Python Number atan() Method:

#!/usr/bin/python
import math

print "atan(0.64) : ",  math.atan(0.64)
print "atan(0) : ",  math.atan(0)
print "atan(10) : ",  math.atan(10)
print "atan(-1) : ",  math.atan(-1)
print "atan(1) : ",  math.atan(1)

Output:
atan(0.64) :  0.569313191101
atan(0) :  0.0
atan(10) :  1.4711276743
atan(-1) :  -0.785398163397
atan(1) :  0.785398163397
------------------------------------------------------------
4. atan2(y, x) : Return atan(y / x), in radians.


Python Number atan2() Method:

#!/usr/bin/python
import math

print "atan2(-0.50,-0.50) : ",  math.atan2(-0.50,-0.50)
print "atan2(0.50,0.50) : ",  math.atan2(0.50,0.50)
print "atan2(5,5) : ",  math.atan2(5,5)
print "atan2(-10,10) : ",  math.atan2(-10,10)
print "atan2(10,20) : ",  math.atan2(10,20)

Output:
atan2(-0.50,-0.50) :  -2.35619449019
atan2(0.50,0.50) :  0.785398163397
atan2(5,5) :  0.785398163397
atan2(-10,10) :  -0.785398163397
atan2(10,20) :  0.463647609001
------------------------------------------------------------
5. cos(x) : Return the cosine of x radians.

Python Number cos() Method:

#!/usr/bin/python
import math

print "cos(3) : ",  math.cos(3)
print "cos(-3) : ",  math.cos(-3)
print "cos(0) : ",  math.cos(0)
print "cos(math.pi) : ",  math.cos(math.pi)
print "cos(2*math.pi) : ",  math.cos(2*math.pi)

Output:
cos(3) :  -0.9899924966
cos(-3) :  -0.9899924966
cos(0) :  1.0
cos(math.pi) :  -1.0
cos(2*math.pi) :  1.0
------------------------------------------------------------
6. hypot(x, y) : Return the Euclidean norm, sqrt(x*x + y*y).

Python Number hypot() Method:
#!/usr/bin/python
import math

print "hypot(3, 2) : ",  math.hypot(3, 2)
print "hypot(-3, 3) : ",  math.hypot(-3, 3)
print "hypot(0, 2) : ",  math.hypot(0, 2)

Output:
hypot(3, 2) :  3.60555127546
hypot(-3, 3) :  4.24264068712
hypot(0, 2) :  2.0

------------------------------------------------------------
7. sin(x) : Return the sine of x radians.

Python Number sin() Method:

#!/usr/bin/python
import math

print "sin(3) : ",  math.sin(3)
print "sin(-3) : ",  math.sin(-3)
print "sin(0) : ",  math.sin(0)
print "sin(math.pi) : ",  math.sin(math.pi)
print "sin(math.pi/2) : ",  math.sin(math.pi/2)

Output:
sin(3) :  0.14112000806
sin(-3) :  -0.14112000806
sin(0) :  0.0
sin(math.pi) :  1.22460635382e-16
sin(math.pi/2) :  1
------------------------------------------------------------
8. tan(x) : Return the tangent of x radians.

Python Number tan() Method:

#!/usr/bin/python
import math

print "tan(3) : ",  math.tan(3)
print "tan(-3) : ",  math.tan(-3)
print "tan(0) : ",  math.tan(0)
print "tan(math.pi) : ",  math.tan(math.pi)
print "tan(math.pi/2) : ",  math.tan(math.pi/2)
print "tan(math.pi/4) : ",  math.tan(math.pi/4)

Output:
tan(3) :  -0.142546543074
tan(-3) :  0.142546543074
tan(0) :  0.0
tan(math.pi) :  -1.22460635382e-16
tan(math.pi/2) :  1.63317787284e+16
tan(math.pi/4) :  1.0
------------------------------------------------------------
9. degrees(x) : Converts angle x from radians to degrees.

Python Number degrees() Method:
#!/usr/bin/python
import math

print "degrees(3) : ",  math.degrees(3)
print "degrees(-3) : ",  math.degrees(-3)
print "degrees(0) : ",  math.degrees(0)
print "degrees(math.pi) : ",  math.degrees(math.pi)
print "degrees(math.pi/2) : ",  math.degrees(math.pi/2)
print "degrees(math.pi/4) : ",  math.degrees(math.pi/4)

Output:
degrees(3) :  171.887338539
degrees(-3) :  -171.887338539
degrees(0) :  0.0
degrees(math.pi) :  180.0
degrees(math.pi/2) :  90.0
degrees(math.pi/4) :  45.0
------------------------------------------------------------

10. radians(x) : Converts angle x from degrees to radians.

Python Number radians() Method:

#!/usr/bin/python
import math

print "radians(3) : ",  math.radians(3)
print "radians(-3) : ",  math.radians(-3)
print "radians(0) : ",  math.radians(0)
print "radians(math.pi) : ",  math.radians(math.pi)
print "radians(math.pi/2) : ",  math.radians(math.pi/2)
print "radians(math.pi/4) : ",  math.radians(math.pi/4)

Output:
radians(3) :  0.0523598775598
radians(-3) :  -0.0523598775598
radians(0) :  0.0
radians(math.pi) :  0.0548311355616
radians(math.pi/2) :  0.0274155677808
radians(math.pi/4) :  0.0137077838904
------------------------------------------------------------
