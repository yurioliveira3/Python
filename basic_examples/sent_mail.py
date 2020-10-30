#! /usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import mysql.connector

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mydb = mysql.connector.connect(host = "host", user = "usr", passwd = "pwd", database = "db")
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
sql_query1 = "SELECT name FROM companie"
mycursor.execute(sql_query1)
name = mycursor.fetchall()

name_res = str(name[0])
name_res = name_res.replace('(u','[').replace(',)',']')

user = username
password = password

list_ =[ #list of mails
   '1'+'-yuri.alves',
   '2'+'-test.test'
   #'3'...
]
   
sent = str(raw_input("Input the prefix mail name here [name.surname]\n 0 if the name not in the list")) #whom to send the email

if sent == '0':
  sent = raw_input("[name.surname]\n")
elif sent == '1':
  sent = 'yuri.alves'


sent_from = user 
send_to = [''+sent+'@xxx.com'] #email addresses
msg = MIMEMultipart('alternative') #message container
msg['Subject'] = subject
msg['From'] = sent_from
msg['To'] = ", ".join(send_to)

# Text
query_usernames = SQL_QUERY
usernames = mycursor2.execute(query_usernames)
usernames = mycursor2.fetchall()

html = """\
<html>
  <head>
  </head>
  <body>
    <table rules="all" style="border-color: #666;" cellpadding="5">
        <tr><th><strong>Nome:</strong></th>
        <th><strong>Usuario:</strong></th>
        <th><strong>Senha:</strong></td></tr> 
"""

for username in usernames:
    html += "<tr>"
    html += "<td>" + username[0].encode('ascii', 'ignore') + "</td>"
    html += "<td>" + username[1] + "</td>"
    html += "</tr>"
    
html += """
    </table>
  </body>
</html>
"""

part1 = MIMEText(html,'html')
msg.attach(part1)

try:
    server = smtplib.SMTP('mail.xxx.com', port)  #specifying mail deliver here
    server.starttls()
    server.ehlo()
    server.login(user, password)
    server.sendmail(sent_from, send_to, msg.as_string())
    server.close()
    print('Email(s) Sent')

except Exception as e:
    print(e)