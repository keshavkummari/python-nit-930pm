import smtplib
import easyemail

sender = "enrique.abiel@gmail.com"
receiver = ['keshav.kummari@gmail.com','asheerapps@gmail.com ','srinivasalaparthi2@gmail.com ','chukkalurisandhya@gmail.com ','aguturu@gmail.com ']
message = "Hello!"

try:
    session = smptlib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender,'Nit@123456')
    session.sendmail(sender,receiver,message)
    session.quit()
except SMTPException:
    print('Error')

"""
#!/usr/bin/python
import smtplib

gmail_user = 'enrique.abiel@gmail.com'
gmail_password = 'Nit@123456'

from_1=gmail_user

to = ['keshav.kummari@gmail.com','asheerapps@gmail.com ','srinivasalaparthi2@gmail.com ','chukkalurisandhya@gmail.com ','aguturu@gmail.com ']

subject = 'Sending Email using GMAIL Mail Server-KeshavKummari'

body = 'Hi, \n  This is a Email Test \n Thanks, \nRoot.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (from_1, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    #server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(from_1, to, email_text)
    server.close()
    print ('Email sent!')
except:
    print ('Something went wrong...')
"""