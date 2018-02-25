import smtplib

content = 'example email stuff here'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('username','password')

mail.sendmail('sender', 'recipienmt', msg2)

mail.close()