#!/usr/bin/python

import MySQLdb

database = "linux"
username = 'root'
password = 'redhat'

# Open database connection
db = MySQLdb.connect(unix_socket='/var/lib/mysql/mysql.sock', host='localhost', user=username, passwd=password, db=database )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select * from test_minnu.my;"

try:
   cursor.execute(sql)
   results = cursor.fetchall()
   print "<table style='width:100%'>"
   for row in results:
      FIRST_NAME  = row[0]
      LAST_NAME = row[1]
      AGE  = row[2]
      GENDER  = row[3]
      INCOME = row[4]
      print "<tr><td>%d</td><td>%s</td><td>%d</td><td>%s</td></tr>"%  ("FIRST_NAME,LAST_NAME,AGE,SEX,INCOME")

   print "</table>"
except:
   print "Error: unable to fecth data"

db.close()

