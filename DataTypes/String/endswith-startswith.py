"""
6	endswith(suffix, beg=0, end=len(string))
	Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
	
33	startswith(str, beg=0,end=len(string))
	Determines if string or a substring of string
	(if starting index beg and ending index end are given)
	starts with substring str; returns true if so and false otherwise.
		
"""

fnames = "Guido Van Rossum Python Perl AWS Azure DevOps"

print(len(fnames))

print(fnames.startswith("guido",0,45))
print(fnames.endswith("devOps",0,45))
