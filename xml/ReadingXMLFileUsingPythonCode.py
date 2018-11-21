#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("F:\\KeshavKummari\\Python_Classroom_and_Online\\DAY-19_XML_Processing\\course.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

# Get all the students in the details
students = collection.getElementsByTagName("course")

# Print detail of each movie.
for a in students:
   print ("*****course*****")
   if a.hasAttribute("title"):
      print ("Title: %s" % a.getAttribute("title"))

   type = a.getElementsByTagName('MONITORINGTOOLS')[0]
   print ("Monitoring Tools: %s" % type.childNodes[0].data)
   format = a.getElementsByTagName('TICKETINGTOOLS')[0]
   print ("Ticketing Tools: %s" % format.childNodes[0].data)
   rating = a.getElementsByTagName('BUGTRACKINGTOOLS')[0]
   print ("Bug Tracking Tools: %s" % rating.childNodes[0].data)
   
