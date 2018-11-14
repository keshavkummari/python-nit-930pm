#!/usr/bin/python

import smtplib

TO='keshav.kummari@gmail.com'
SUBJECT='Send email using SMTPLIB in Python'
TEXT='Here is the message we would like to send'

# Gmail Credentials:
gmail_sender='keshavckk@gmail.com'
gmail_passwd='Admin@123'

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo
server.login(gmail_sender,gmail_passwd)

BODY='\r\n'.join([
    'To: %s' % TO,
    'From: %s' % gmail_sender,
    'Subject: %s' % SUBJECT,
    '',
    TEXT
    ])
try:
    server.sendmail(gmail_sender,[TO],BODY)
    print('email sent')
except:
    print('error sending email')

sever.quit()    
