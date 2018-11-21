#!/usr/bin/python
import xml.etree.ElementTree as ET

input ='''
<stuff>
<users>
    <user x="2">
          <id>001</id>
          <name>Minnu</name>
    </user>
    <user x="7">
          <id>002</id>
          <name>Abiel</name>
    </user>     
</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print ("User Count: ", len(lst))

for item in lst:
    print ("Name", item.find("name").text)
    print ("Id", item.find("id").text)
    print ("Attribute", item.get("x"))
    
'''Output:
User Count:  2
Name Minnu
Id 001
Attribute 2
Name Abiel
Id 002
Attribute 7
'''
