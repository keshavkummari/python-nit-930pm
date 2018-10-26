# Python dictionary:

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

minnu_dict = {'Name':'minnu', 'Age': 7, 'Class': 'First'}
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

print ("dict['Course']: ", dict_1['Course'])

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

dictionary len() Function:

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
dictionary str() Function:

The method str() produces a printable string representation of a dictionary.

Syntax: str(dict)

dict -- This is the dictionary.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7};
print "Equivalent String : %s" % str (dict)

Output:
Equivalent String : {'Age': 7, 'Name': 'minnu'}
-----------------------------------------------------------------
dictionary type() Function:

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

The method has_key() returns true if a given key is
available in the dictionary, otherwise it returns a false.

Syntax: dict.has_key(key)

key -- This is the Key to be searched in the dictionary.

#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print "Value : %s" %  dict.has_key('Age')
print "Value : %s" %  dict.has_key('Gender')

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

print ("Value : %s" %  dict.keys())

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
