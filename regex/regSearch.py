#!/usr/bin/python

import re

whoinvented = "Python Was Created by Guido Van Rossum"

_a = re.search('(.*)KUMMARI|Was(.*)',whoinvented,re.IGNORECASE|re.M)

if _a:
	print(_a.group())
	print(_a.groups())
else:
	print("Condition is not met")
