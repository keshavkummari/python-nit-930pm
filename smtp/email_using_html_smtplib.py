#!/usr/bin/python
import smtplib

print ('''

  ________               .__.__   
 /  _____/  _____ _____  |__|  |  
/   \  ___ /     \\__  \ |  |  |  
\    \_\  \  Y Y  \/ __ \|  |  |__
 \______  /__|_|  (____  /__|____/
        \/      \/     \/         
                           File  send
               Coder by Keshav Kummari
''') 


sender = 'root@py33.minnu.com'
receivers = ['keshavk@py33.minnu.com']

message = """From: From Person <root@py33.minnu.com>
To: To Person <keshav.kummari@py33.minnu.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
