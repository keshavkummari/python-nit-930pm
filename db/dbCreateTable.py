#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat@123")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
sql = """CREATE TABLE `python_9pm`.students
      (ID INT,FNAME VARCHAR(30),LNAME VARCHAR(30),AGE VARCHAR(30),
      ADDRESS VARCHAR(20),FEE INT);"""

cursor.execute(sql)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Table has been created : %s " % data)

# disconnect from server
db.close()


INSERT INTO `python_9pm`.students(ID,FNAME,LNAME,AGE,ADDRESS,FEE) VALUES (1,'Guido','Rossum',48,"LA-32",0090);

