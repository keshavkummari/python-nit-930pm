#!/usr/bin/python

_007 = "Python"

print (len(_007))

print (_007.ljust(10, '*'))   # _007 = python 6  10-python 4=****

print (_007.rjust(10, '*'))   # _007 = python 6  10-python 4=****

print (len(_007))

"""
20	ljust(width[, fillchar])
	Returns a space-padded string with the original string
	left-justified to a total of
	width columns.
"""
