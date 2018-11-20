'''
[root@classroom www]# python -m CGIHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
'''

#!/usr/bin/python

#import mysql.connector
import pymysql

# Open database connection
db = pymysql.connect("localhost","root","redhat")

#db = MySQLdb.connect("server.minnu.com","root","redhat","test_minnu" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()

"""
  176  systemctl status mariadb.service
  177  yum install mariadb* -y
  178  systemctl status mariadb.service
  179  systemctl enable mariadb.service
  180  systemctl start mariadb.service
  181  systemctl status mariadb.service
  182  ifconfig 
  183  mysql_secure_installation 
  184  mysql -u root -p
  185  mysql -uroot -predhat
  186  firewall-cmd --list-all
  187  firewall-cmd --permanent --add-service=mysql
  188  firewall-cmd --reload 
  189  firewall-cmd --list-all
  190  mysql -uroot -predhat
  191  ifconfig 
  192  hostname
  193  mysql -uroot -predhat
"""
