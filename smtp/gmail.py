import smtplib

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
