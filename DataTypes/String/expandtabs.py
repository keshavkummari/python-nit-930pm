"""
7	expandtabs(tabsize=8)
	Expands tabs in string to multiple spaces; defaults to 8 spaces per tab 
	if tabsize not provided.


technologies = "Java Perl Python DevOps Agile nodejs"

print(technologies.expandtabs(40))	
"""


#!/usr/bin/python

#guido = "this is string example....rock!!!"
guido = "this is\tstring example....rock!!!"

print ("Original string: ", guido)

print("")

print ("Defualt exapanded tab# ",guido.expandtabs())

print("")

print ("Double exapanded tab= ",guido.expandtabs(40))


"""
str.expandtabs(tabsize=8)
Expands tabs in string to multiple spaces;
defaults to 8 spaces per tab if tabsize not provided.
"""
