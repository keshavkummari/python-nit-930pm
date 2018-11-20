#!/usr/bin/python3

import MySQLdb

# Open database connection
db = MySQLdb.connect("13.232.171.167","root","redhat@123")

#db = MySQLdb.connect("HOSTNAME/IP","USERNAME","PASSWORD")
#db = MySQLdb.connect("localhost","root","redhat","linux" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()
