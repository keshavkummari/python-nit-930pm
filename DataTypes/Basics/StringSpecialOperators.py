# String Special Operators:
                                 0  1  2  3  4 # Left to Right index
								-5 -4 -3 -2 -1 # Right to Left index
                     firstname ="G  u  i  d  o"
Assume string variable a holds ' H e l l o' and variable b holds 'Python', then :

Operator    : +
Description : Concatenation - Adds values on either side of the operator
Example     : a + b will give HelloPython

Operator    : *
Description : Repetition - Creates new strings,
              concatenating multiple copies of the same string
Example     : a*2 will give -HelloHello

Operator    : []
Description : Slice - Gives the character from the given index
Example     : a[1] will give e

Operator    : [ : ]  # [0:end-1]  [0:5-1(4)] [:5] 5-1 01234
Description : Range Slice - Gives the characters from the given range
Example     :   a[1:4] will give ell

Operator    : r/R
Description : Raw String - Suppresses actual meaning of Escape characters.
The syntax for raw strings is exactly the same as for normal strings with
the exception of the raw string operator, the letter "r,"
which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and
must be placed immediately preceding the first quote mark.

Example     : print(r'\n') prints(\n) and print(R'\n') prints(\n)

Operator    :  %
Description :  Format - Performs String formatting
********************************************************************
# String Formatting Operator :
One of Pythons coolest features is the string format operator %.

This operator is unique to strings and makes up for the pack of having functions
from C's printf() family.

#!/usr/bin/python

print ("My name is %s and I born in %d" % ('Python', 1981))