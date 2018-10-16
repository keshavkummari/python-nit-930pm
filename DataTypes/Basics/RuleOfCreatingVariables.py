#!/usr/bin/python

#! = Shebang
# /usr/bin/python = Absolute path of the python

# Creating variables in python

# A-Z     # Hash means single line comment
# a-z
# combinations of A-Z & a-z
# 0-9
# combinations of A-Z , a-z & 0-9
# an underscore (_).
# combinations of A-Z , a-z , 0-9 & _

# Below is the multi-line comment """ """ or ''' ''''

"""We can use camel-case style i.e.,
capitalize every first letter of the word
except the initial word without any spaces."""

'''This is
multi-line
comment'''


# Single-Line Comments : 1. #, 2. '', 3. " ", 4. ''' ''' & 5. """ """

# Multi-Line Comments : 1. ''' ''' & 2. """ """

# Creating Variables in Python

#FIRSTNAME = "Guido"
#middlename = 'Van'
#LastName = '''Rossum'''
#_programmingLang = """Python 3.6.0"""
"""
'Calling or Accessing Variables in Python'

print(FIRSTNAME)
print('Firstname : ',FIRSTNAME,"@Python")
print(FIRSTNAME,"Firstname Variable has called")
print('Calling a Variable : ',FIRSTNAME)

print("FirstName  : ",FIRSTNAME, "MiddleName : ", middlename, 'LastName :', LastName,'Programming Language : ',_programmingLang)
"""
FIRSTNAME,middlename,LastName,_programmingLang = "Guido",'Van','''Rossum''',"""Python 3.6.0"""

#FIRSTNAME = middlename = LastName = _programmingLang = '01929292'

print(FIRSTNAME,type(FIRSTNAME),id(FIRSTNAME))
print(middlename,type(middlename),id(middlename))
print(LastName,type(LastName),id(LastName))
print(_programmingLang,type(_programmingLang),type(_programmingLang))


