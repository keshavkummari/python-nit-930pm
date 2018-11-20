#!/usr/bin/python


import pymysql.connector

from pymysql.connector import errorcode

try:
  db = pymysql.connector.connect(user='root', password='redhat',
                                host='127.0.0.1', database='world')
except pymysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Acess denied/wrong  user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  db.close()