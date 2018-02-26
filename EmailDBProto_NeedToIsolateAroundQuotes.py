import smtplib
import sqlite3


conn = sqlite3.connect('StriveDB.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT Msg FROM Motivational')
info2 = cur2.fetchall()

print(info2)