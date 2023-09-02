import smtplib
from email.message import EmailMessage
import mailconfig

sender = mailconfig.myaddress
pswd = mailconfig.smtppswd
servername = mailconfig.smtpservername
port = mailconfig.port
tos = mailconfig.tos

print('server connection...  ',end='') 
server = smtplib.SMTP(servername, port)
server.starttls()
print('Ok')

print('message generator...  ',end='')    
msg = EmailMessage()
text = 'Code to authentication is %d' % 1
msg['Subject'] = f'The contents of [number]'
msg['From'] = sender
msg['To'] = tos
msg.set_content(text)
print('Ok')

print('loggining...  ',end='')
server.login(sender,pswd)
print('Ok')
print('sending...  ',end='')
server.send_message(msg)
print('Ok')