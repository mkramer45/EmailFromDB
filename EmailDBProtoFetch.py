import smtplib
import sqlite3


conn = sqlite3.connect('StriveDB.db')
cursor = conn.cursor()
cursor.execute('SELECT Msg FROM Motivational')
row = cursor.fetchall()


mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('username','pw')

mail.sendmail('sender', 'recipient', row)

mail.close()

conn.commit()
cursor.close()
conn.close()
