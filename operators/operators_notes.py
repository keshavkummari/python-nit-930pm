# ---------------------- PYTHON ------------------------------- #
  -------[ Keshav Kummari | Email_id: keshav.kummari@gmail.com ] ------------
# --------------------------------------------------------------------------- #

# Python Operators:

# There are 7 types of Operators :

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

'''--------------------------------------------------------------'''
# 1. Arithmetic Operators:
'''--------------------------------------------------------------'''
1. +   =	Addition
2. -   =	Subtraction
3. *   =	Multiplication
4. /   =	Division  
5. %   =	Modulus
6. **  =	Exponent
7. //  =	Floor Division

'''--------------------- Examples ----------------------------'''
# Example #1: Arithmetic operators in Python
x = 15
y = 4

print('x + y =',x+y) # Output: x + y = 19
print('x - y =',x-y) # Output: x - y = 11
print('x * y =',x*y) # Output: x * y = 60
print('x / y =',x/y) # Output: x / y = 3.75  Division
print('x // y =',x//y) # Output: x // y = 3  Floor Division
print('x ** y =',x**y) # Output: x ** y = 50625 Exponent
print('x % y =',x%y) # Output: x % y = 3  Modulus
OUTPUT:
x + y = 19
x - y = 11
x * y = 60
x / y = 3.75
x // y = 3
x ** y = 50625
x % y = 3
'''--------------------------------------------------------------'''
# 2. Comparison (Relational) Operators :
'''--------------------------------------------------------------'''
a = 10 
b = 20

1. ==	= (a == b) is not true.
2. !=	= (a != b) is true.
3. >	= (a > b) is not true.
4. <	= (a < b) is true.
5. >=	= (a >= b) is not true.
6. <=	= (a <= b) is true.

'''--------------------- Examples ----------------------------'''
# Comparison operators in Python

# Example: 
x = 10
y = 12

print('x > y  is',x>y) # Output: x > y is False
print('x < y  is',x<y) # Output: x < y is True
print('x == y is',x==y)# Output: x == y is False
print('x != y is',x!=y)# Output: x != y is True
print('x >= y is',x>=y)# Output: x >= y is False
print('x <= y is',x<=y)# Output: x <= y is True

OUTPUT:
x > y  is False
x < y  is True
x == y is False
x != y is True
x >= y is False
x <= y is True


'''--------------------------------------------------------------'''
# 3. Assignment Operators :
'''--------------------------------------------------------------'''
# Assignment operators are used in Python to assign values to variables.
'''
a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.
There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. 
'''
-------------------------------------------
Operator |	    Example	 |	Equivatent to
-------------------------------------------
1.   =			x = 5		x = 5
2.  +=			x += 5		x = x + 5	[+= Add AND]
3.  -=			x -= 5		x = x - 5	[-= Subtract AND]
4.  *=			x *= 5		x = x * 5	[*= Multiply AND]
5.  /=			x /= 5		x = x / 5	[/= Divide AND]
6.  %=			x %= 5		x = x % 5	[%= Modulus AND]
7.  //=			x //= 5		x = x // 5	[//= Floor Division]
8.  **=			x **= 5		x = x ** 5	[**= Exponent AND]
9.  &=			x &= 5		x = x & 5    ### NOOOOOOOTTTEEEEEE
10. |=			x |= 5		x = x | 5
11. ^=			x ^= 5		x = x ^ 5
12. >>=			x >>= 5		x = x >> 5
13. <<=			x <<= 5		x = x << 5

-------------------------------------------
# Example : 

# Assume variable a holds the value 10 and variable b holds the value 20 :

c = a + b assigns value of a + b into c

# += Add AND	: It adds right operand to the left operand and assign the result to left operand	

# Example : c += a is equivalent to c = c + a

a = 10
b = 20

c = a + b	# a + b assigns value of a + b into c
c += a		# c += a is equivalent to c = c + a

# -= Subtract AND : It subtracts right operand from the left operand and assign the result to left operand

c -= a 		# c -= a is equivalent to c = c - a

'''--------------------------------------------------------------'''
#!/usr/bin/python3
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c )

c *= a
print ("Line 3 - Value of c is ", c )

c /= a 
print ("Line 4 - Value of c is ", c )

c  = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)

OUTPUT:
Line 1 - Value of c is  31
Line 2 - Value of c is  52
Line 3 - Value of c is  1092
Line 4 - Value of c is  52.0
Line 5 - Value of c is  2
Line 6 - Value of c is  2097152
Line 7 - Value of c is  99864

'''--------------------------------------------------------------'''
# 4. Logical Operators :
'''--------------------------------------------------------------'''
# Example:  variable a holds True and variable b holds False

1. and Logical AND		= (a and b) is False.
2. or Logical OR		= (a or b) is True.
3. not Logical NOT		= Not(a and b) is True.

'''--------------------- Examples ----------------------------'''
# Example : Logical Operators in Python

x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)

OUTPUT:
x and y is False
x or y is True
not x is False
'''--------------------------------------------------------------'''
# 5. Bitwise Operators :
'''--------------------------------------------------------------'''
Bitwise operator works on bits and performs bit-by-bit operation. 

Assume if a = 60 and b = 13

Now in binary format they will be as follows :
a = 0011 1100
b = 0000 1101

# Note: Python's built-in function bin() can be used to obtain binary
representation of an integer number.

For example, 2 is 10 in binary and 7 is 111.

In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

# Bitwise operators in Python :

Operator	Meaning	Example
1. &			Bitwise AND	x & y = 0 (0000 0000)
2. |			Bitwise OR	x | y = 14 (0000 1110)
3. ~			Bitwise NOT	~x = -11 (1111 0101)
4. ^			Bitwise XOR	x ^ y = 14 (0000 1110)
5. >>			Bitwise right shift	x>> 2 = 2 (0000 0010)
6. <<			Bitwise left shift	x<< 2 = 40 (0010 1000)

'''--------------------- Examples ----------------------------'''

#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        # 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))

c = a | b;        # 61 = 0011 1101 
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))


OUTPUT:
a = 60 : 0b111100 b = 13 : 0b1101
result of AND is  12 : 0b1100
result of OR is  61 : 0b111101
result of EXOR is  49 : 0b110001
result of COMPLEMENT is  -61 : -0b111101
result of LEFT SHIFT is  240 : 0b11110000
result of RIGHT SHIFT is  15 : 0b111

'''--------------------------------------------------------------'''
# 6. Membership Operators :
'''--------------------------------------------------------------'''

'''
in and not in are the membership operators in Python. 

They are used to test whether a value or variable is found in a sequence
(string, list, tuple, set and dictionary).
'''
# Membership operators test for membership in a sequence, such as
# strings, lists, or tuples.

1. in	    = x in y, here in results in a 1 if x is a member of sequence y.
2. not in   = x not in y, here not in results in a 1 if x is not a member of sequence y.

'''--------------------- Examples ----------------------------'''
Example #5: Membership operators in Python

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

OUTPUT :
True
True
True
False
'''--------------------------------------------------------------'''
# 7. Identity Operators :
'''--------------------------------------------------------------'''

'''
is and is not are the identity operators in Python. 

They are used to check if two values (or variables) are located on the same part of the memory. 

Two variables that are equal does not imply that they are identical.
'''
# Identity operators compare the memory locations of two objects.

1. is		= x is y, here is results in 1 if id(x) equals id(y).
2. is not	= x is not y, here is not results in 1 if id(x) is not equal to id(y).

'''--------------------- Examples ----------------------------'''
# Example : Identity operators in Python

x1 = 5
y1 = 5

x2 = 'Hello'
y2 = 'Hello'

x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

OUTPUT : 
False
True
False

# ---------------------- PYTHON SET DATA TYPE ------------------------------- #
  -------[ Keshav Kummari | Email_id: keshav.kummari@gmail.com ] ------------
# --------------------------------------------------------------------------- #

