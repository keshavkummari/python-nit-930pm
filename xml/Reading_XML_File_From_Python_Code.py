# A simple XML file, later parse it with Python minidom.
'''
staff.xml
<?xml version="1.0"?>
<company>
	<name>Mkyong Enterprise</name>
	<staff id="1001">
		<nickname>mkyong</nickname>
		<salary>100,000</salary>
	</staff>
	<staff id="1002">
		<nickname>yflow</nickname>
		<salary>200,000</salary>
	</staff>
	<staff id="1003">
		<nickname>alex</nickname>
		<salary>20,000</salary>
	</staff>
</company>
'''
"""
<?xml version="1.0"?>
<company>
	<name>Online Ucator</name>
	<staff id="1001">
		<nickname>Minnu</nickname>
		<salary>100,000</salary>
	</staff>
	<staff id="1002">
		<nickname>Keshav</nickname>
		<salary>200,000</salary>
	</staff>
	<staff id="1003">
		<nickname>Jessi</nickname>
		<salary>20,000</salary>
	</staff>
</company>
"""
#2. DOM Example 1
#A simple Python minidom example.

# dom-example.py
from xml.dom import minidom

doc = minidom.parse("staff.xml")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]

print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")

for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))








