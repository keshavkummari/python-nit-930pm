#2. DOM Example 1
#A simple Python minidom example.

# dom-example.py
from xml.dom import minidom

doc = minidom.parse("C:\\Users\\Jessicah Princess\\Desktop\\dom_example.xml")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

first = doc.getElementsByTagName("staff")
for staff in first:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))

