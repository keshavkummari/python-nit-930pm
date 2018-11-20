#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("54.163.174.204","root","redhat@123")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create SCHEMA as per requirement
sql = "create database python_9pm;"

cursor.execute(sql)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("SCHEMA has been created : %s " % data)

# disconnect from server
db.close()



