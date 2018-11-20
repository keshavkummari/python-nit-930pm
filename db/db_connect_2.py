#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS users")

#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE test_minnu.users (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         Gender CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Table has been created : %s " % data)

# disconnect from server
db.close()



