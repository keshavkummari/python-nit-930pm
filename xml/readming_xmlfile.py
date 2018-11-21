#!/usr/bin/python

from xml.dom import minidom
xmldoc = minidom.parse('xml_file.xml')
itemlist = xmldoc.getElementsByTagName('item') 
print ("Len : ", len(itemlist))
print ("Attribute Name : ", itemlist[0].attributes['name'].value)
print ("Text : ", itemlist[0].firstChild.nodeValue)
for s in itemlist :
    print ("Attribute Name : ", s.attributes['name'].value)
    print ("Text : ", s.firstChild.nodeValue)
