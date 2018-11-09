"""
Example text, file.txt: Python

aaaa
bbbbb
aaaa
bbbbb
aaaa bbbbb
CCcc
xx
y y y y y
Z

Python program that counts characters in file
"""
# Open a file.
f = open(r"C:\programs\file.txt", "r")

# Stores character counts.
chars = {}

# Loop over file and increment a key for each char.
for line in f.readlines():
    for c in line.strip():
	# Get existing value for this char or a default of zero.
	# ... Add one and store that.
	chars[c] = chars.get(c, 0) + 1

# Print character counts.
for item in chars.items():
    print(item)

"""
Output

('a', 12)
(' ', 5)
('C', 2)
('b', 15)
('c', 2)
('y', 5)
('x', 2)
('Z', 1)
"""


