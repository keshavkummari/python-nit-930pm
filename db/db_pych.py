#!/usr/bin/python


import pyMySQL

# Open database connection
db = pyMySQL.connect("localhost","root","redhat")
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
