#!/usr/bin/python

import re

firstname = "Python Was Created by Guido Van Rossum"

middleName = "Van"

lastname = "Rossum"

_a = re.match('(.*)GUIDO(.*)',firstname,re.I|re.M)

if _a:
	print(_a.group())
	print(_a.groups())
	print(type(_a))
	print(id(_a))
else:
	print("Condition is not met")
