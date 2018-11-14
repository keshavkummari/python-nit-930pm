#!/usr/bin/python

import smtplib

sender = 'root@server0.example.com'
receivers = ['jay@server0.example.com','sandeep@server0.example.com','vamshi@server0.example.com']

message = """From: From Person <root@server0.example.com>
To: To Person <jay@server0.example.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
