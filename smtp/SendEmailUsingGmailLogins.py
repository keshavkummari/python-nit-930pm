import smtplib

try:  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
except:  
    print ('Something went wrong...')

import smtplib

try:  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # ...send emails
except:  
    print ('Something went wrong...')

import smtplib

gmail_user = 'keshavckk@gmail.com'  
gmail_password = 'Admin@123'

from_1=gmail_user
to = ['keshav.kummari@gmail.com','enrique.abiel@gmail.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, whats up?\n\n- You'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (from_1, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(from_1, to, email_text)
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')
