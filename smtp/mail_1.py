import smtplib

content = 'example'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('email','password')

mail.sendmail('fromemail','receiver',content)
