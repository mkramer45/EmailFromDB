import smtplib
import sqlite3


conn = sqlite3.connect('StriveDB.db')
cursor = conn.cursor()
msg2 = cursor.execute('select Msg from Motivational')

conn.commit()
cursor.close()
conn.close()

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('username','password')

mail.sendmail('sender', 'recipienmt', msg2)

mail.close()
