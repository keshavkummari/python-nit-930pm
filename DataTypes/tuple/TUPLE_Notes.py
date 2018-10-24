# Python Tuples:

A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 

The differences between tuples and lists are, 
the tuples cannot be changed unlike lists and tuples use parentheses, 
whereas lists use square brackets.

# Tuples are created with the help of comma-separated values between parentheses or without it.

tup1 = ('python', 'linux', 1997, 2000, 55.86)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

The empty tuple is written as two parentheses containing nothing:
tup1 = ()

To write a tuple containing a single value you have to include a comma, 
even though there is only one value :
tup1 = (50,)

Like string indices, tuple indices start at 0, 
and they can be sliced, concatenated, and so on.

-----------------------------------------------------------------
Accessing Values in Tuples:

To access values in tuple, 
use the square brackets for slicing along with the index or indices to obtain
value available at that index. 

#!/usr/bin/python

tup1 = ('python', 'linux', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

Output:
tup1[0]:  python
tup2[1:5]:  [2, 3, 4, 5]

-----------------------------------------------------------------
# Updating Tuples:

Tuples are immutable which means you cannot update
or change the values of tuple elements. 

You are able to take portions of existing tuples to create new tuples.

#!/usr/bin/python
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3)

Output:
(12, 34.56, 'abc', 'xyz')
-----------------------------------------------------------------
Delete Tuple Elements:

Removing individual tuple elements is not possible. 

There is, of course, nothing wrong with putting together another tuple with the undesired elements discarded.

To explicitly remove an entire tuple, just use the del statement. 

#!/usr/bin/python

tup = ('python', 'linux', 1997, 2000)

print (tup)
del tup
print ("After deleting tup : ")
print (tup)

 An exception raised, this is because after del tup tuple does not exist any more :
Output: 

('python', 'linux', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print tup;
NameError: name 'tup' is not defined
-----------------------------------------------------------------
Basic Tuples Operations:

Tuples respond to the + and * operators much like strings; 

they mean concatenation and repetition here too, 

except that the result is a new tuple, not a string.

In fact, tuples respond to all of the general sequence operations we used on strings.

--------------------------------------------------------------------------
Python Expression		Results			    Description
--------------------------------------------------------------------------
len((1, 2, 3))			3			    Length
(1, 2, 3) + (4, 5, 6)		(1, 2, 3, 4, 5, 6)	    Concatenation
('Hi!') * 4			('Hi!', 'Hi!', 'Hi!', 'Hi!')Repetition
3 in (1, 2, 3)			True			    Membership
for x in (1, 2, 3): print x,	1 2 3			    Iteration

--------------------------------------------------------------------------
Indexing, Slicing, and Matrixes:

Because tuples are sequences, indexing and slicing work the 
same way for tuples as they do for strings. 

L = ('spam', 'Spam', 'SPAM!')

-----------------------------------------------------------------
Python Expression	Results			Description
-----------------------------------------------------------------
L[2]			'SPAM!'			Offsets start at zero
L[-2]			'Spam'			Negative: count from the right
L[1:]			['Spam', 'SPAM!']	Slicing fetches sections
-----------------------------------------------------------------
No Enclosing Delimiters:

Any set of multiple objects, comma-separated, written without identifying symbols, 
i.e., brackets for lists, parentheses for tuples, etc., 
default to tuples, as indicated.

#!/usr/bin/python
print 'abc', -4.24e93, 18+6.6j, 'xyz'
x, y = 1, 2;
print "Value of x , y : ", x,y

Output:
abc -4.24e+93 (18+6.6j) xyz
Value of x , y : 1 2
-----------------------------------------------------------------
# Built-in Tuple Functions:

1. Tuple len() Functions:

The method len() returns the number of elements in the tuple.

Syntax : len(tuple)

#!/usr/bin/python

# tuple1, tuple2 = (123, 'xyz', 'minnu'), (456, 'abc')

tuple1=(123, 'xyz', 'minnu')
tuple2=(456, 'abc')

print "First tuple length : ", len(tuple1)
print "Second tuple length : ", len(tuple2)

Output:
First tuple length :  3
Second tuple length :  2
-----------------------------------------------------------------
2. Tuple max() Functions:

The method max() returns the elements from the tuple with maximum value.

Syntax: max(tuple)

#!/usr/bin/python

tuple1, tuple2 = (123, 'xyz', 'minnu', 'abc'), (456, 700, 200)

print "Max value element : ", max(tuple1)
print "Max value element : ", max(tuple2)

Output:
Max value element :  minnu
Max value element :  700
-----------------------------------------------------------------
3. Tuple min() Functions:

The method min() returns the elements from the tuple with minimum value.

Syntax: min(tuple)

tuple -- This is a tuple from which min valued element to be returned.

#!/usr/bin/python

tuple1, tuple2 = (123, 'xyz', 'minnu', 'abc'), (456, 700, 200)

print "min value element : ", min(tuple1)
print "min value element : ", min(tuple2)

Output:
min value element :  123
min value element :  200
-----------------------------------------------------------------
4. Tuple tuple() Functions:

The method tuple() converts a list of items into tuples

Syntax: tuple( seq )

seq -- This is a tuple to be converted into tuple.

#!/usr/bin/python

aList = (123, 'xyz', 'minnu', 'abc');
aTuple = tuple(aList)

print "Tuple elements : ", aTuple

Output:
Tuple elements :  (123, 'xyz', 'minnu', 'abc')
-----------------------------------------------------------------
Python dictionary:

Each key is separated from its value by a colon (:), 
the items are separated by commas, and the whole thing is enclosed in curly braces. 

An empty dictionary without any items is written with just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. 

The values of a dictionary can be of any type, but the keys must be of an immutable
data type such as strings, numbers, or tuples.

-------------------------------------------------------------------
# Accessing Values in dictionary:

To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.


#!/usr/bin/python

minnu_dict = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}
minnu_list = ['Name','minnu','Age',7,'Class','First'] # List 
minnu_tuple = ('Name','minnu','Age',7, 'Class','First') # Tuple

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

Output:
dict['Name']:  minnu
dict['Age']:  7

"""If we attempt to access a data item with a key, which is not part of the dictionary, 
we get an error as follows :"""

#!/usr/bin/python

dict_1 = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print "dict['Course']: ", dict_1['Course']

Output:
dict['Alice']:
Traceback (most recent call last):
   File "test.py", line 4, in <module>
      print "dict['Course']: ", dict['Course'];
KeyError: 'Course'
-----------------------------------------------------------------
Updating dictionary:

You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry.

#!/usr/bin/python

ronnie = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

ronnie['Age'] = 8; # update existing entry
ronnie['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

Output:
dict['Age']:  8
dict['School']:  DPS School

-----------------------------------------------------------------
Delete dictionary Elements:

You can either remove individual dictionary elements or clear the entire contents of a dictionary. 

You can also delete entire dictionary in a single operation.

To explicitly remove an entire dictionary, just use the del statement. 

#!/usr/bin/python
ronnie = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

del ronnie['Name']; # remove entry with key 'Name'

ronnie.clear();     # remove all entries in dict

del ronnie;        # delete entire dictionary

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

That an exception is raised because after del dict dictionary does not exist any more.

Output:

dict['Age']:
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print "dict['Age']: ", dict['Age'];
TypeError: 'type' object is unsubscriptable

**********************************************************************
Properties of dictionary Keys:

dictionary values have no restrictions. 
They can be any arbitrary Python object, either standard objects or user-defined objects. 
However, same is not true for the keys.

There are two important points to remember about dictionary keys:

(a) More than one entry per key not allowed. Which means no duplicate key is allowed. 

When duplicate keys encountered during assignment, the last assignment wins. 

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7, 'Name': 'Manni'}

print "dict['Name']: ", dict['Name']

Output:
dict['Name']:  Manni

Note: Keys must be immutable.
Which means you can use strings, numbers or tuples as dictionary keys but something
like ['key'] is not allowed. 

#!/usr/bin/python

dict_1 = {['Name']: 'minnu', 'Age': 7}

print "dict_1['Name']: ", dict_1['Name']

Output:

Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'minnu', 'Age': 7};
TypeError: list objects are unhashable
-----------------------------------------------------------------
Built-in dictionary Functions & Methods :

dictionary len() Functions:

The method len() gives the total length of the dictionary. 
This would be equal to the number of items in the dictionary.

Syntax: len(dict)

dict -- This is the dictionary, whose length needs to be calculated.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7};
print "Length : %d" % len (dict)

Output:
Length : 2
-----------------------------------------------------------------
dictionary str() Functions:

The method str() produces a printable string representation of a dictionary.

Syntax: str(dict)

dict -- This is the dictionary.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7};
print "Equivalent String : %s" % str (dict)

Output:
Equivalent String : {'Age': 7, 'Name': 'minnu'}
-----------------------------------------------------------------
dictionary type() Functions:

The method type() returns the type of the passed variable. 

If passed variable is dictionary then it would return a dictionary type.

Syntax : type(dict)

Parameters : dict -- This is the dictionary.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7};
print "Variable Type : %s" %  type (dict)

Output:
Variable Type : <type 'dict'>
-----------------------------------------------------------------
dictionary clear() Method:

The method clear() removes all items from the dictionary.

Syntax: dict.clear()

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7};

print "Start Len : %d" %  len(dict)
dict.clear()
print "End Len : %d" %  len(dict)

Output:
Start Len : 2
End Len : 0
-----------------------------------------------------------------
dictionary copy() Method:

The method copy() returns a shallow copy of the dictionary.

Syntax: dict.copy()

#!/usr/bin/python

dict1 = {'Name': 'minnu', 'Age': 7};

dict2 = dict1.copy()
print "New dictinary : %s" %  str(dict2)

Output:
New dictinary : {'Age': 7, 'Name': 'minnu'}
-----------------------------------------------------------------
dictionary fromkeys() Method:

The method fromkeys() creates a new dictionary with keys from seq and values set to value.

Syntax: dict.fromkeys(seq[, value]))

seq -- This is the list of values which would be used for dictionary keys preparation.
value -- This is optional, if provided then value would be set to this value

#!/usr/bin/python

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print "New dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq, 10)
print "New dictionary : %s" %  str(dict)

Output:
New dictionary : {'age': None, 'name': None, 'sex': None}
New dictionary : {'age': 10, 'name': 10, 'sex': 10}
-----------------------------------------------------------------
dictionary get() Method:

The method get() returns a value for the given key. 
If key is not available then returns default value None.

Syntax : dict.get(key, default=None)

key -- This is the Key to be searched in the dictionary.
default -- This is the Value to be returned in case key does not exist.

#!/usr/bin/python

dict = {'Name': 'Zabra', 'Age': 7}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Education', "Never")

Output:
Value : 7
Value : Never

-----------------------------------------------------------------
dictionary has_key() Method:

The method has_key() returns true if a given key is available in the dictionary, 
otherwise it returns a false.

Syntax: dict.has_key(key)

key -- This is the Key to be searched in the dictionary.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print "Value : %s" %  dict.has_key('Age')
print "Value : %s" %  dict.has_key('Sex')

Output:
Value : True
Value : False
-----------------------------------------------------------------
dictionary items() Method:

The method items() returns a list of dict's (key, value) tuple pairs

Syntax: dict.items()

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print "Value : %s" %  dict.items()

Output:
Value : [('Age', 7), ('Name', 'minnu')]
-----------------------------------------------------------------
dictionary keys() Method:

The method keys() returns a list of all the available keys in the dictionary.

Syntax :dict.keys()

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print "Value : %s" %  dict.keys()

Output:
Value : ['Age', 'Name']
-----------------------------------------------------------------
dictionary setdefault() Method:

The method setdefault() is similar to get(), but will set dict[key]=default
if key is not already in dict.

Syntax: dict.setdefault(key, default=None)

key -- This is the key to be searched.
default -- This is the Value to be returned in case key is not found.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print "Value : %s" %  dict.setdefault('Age', None)
print "Value : %s" %  dict.setdefault('Sex', None)

Output:
Value : 7
Value : None
-----------------------------------------------------------------
dictionary update() Method:

The method update() adds dictionary dict2's key-values pairs in to dict.

Syntax: dict.update(dict2)

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print "Value : %s" %  dict

Output:
Value : {'Age': 7, 'Name': 'minnu', 'Sex': 'female'}
-----------------------------------------------------------------
dictionary values() Method:

The method values() returns a list of all the values available in a given dictionary.

Syntax : dict.values()

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print "Value : %s" %  dict.values()

Output:
Value : [7, 'minnu']
-----------------------------------------------------------------
