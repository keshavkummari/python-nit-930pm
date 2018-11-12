import re

"""
# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24 August 9 Dec 12",re.M|re.I)

for i in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (i))

# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"

matches = re.findall(regex, "June 24, August 9, Dec 12")

for i in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print ("Match month: %s" % (i))

"""
# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"

matches = re.finditer(regex, "June 24, August 9, Dec 12")

for i in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print ("Match at index: %s, %s" % (i.start(), i.end()))





