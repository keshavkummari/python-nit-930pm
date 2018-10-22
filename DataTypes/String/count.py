"""
3	count(str, beg= 0,end=len(string))
	Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
"""

name = "Guido Van Rossum"

print(name,type(name),id(name),len(name))

check="s"

print(name.count(check,0,5))

print(name.count("o",0,17))
