'''
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
text = """Test 1A: Start QWERTY"""
msg['Subject'] = 'Test 1A'
msg['From'] = sender
msg.set_content(text)
print('Ok')

print('loggining...  ',end='')
server.login(sender,pswd)
print('Ok')
msg['To'] = tos
server.send_message(msg)

"""
for (index,mail) in enumerate(tos):      
    print(f'sending to {mail}... ',end='')
    #msg['To'] = mail
    #server.send_message(msg)
    del msg['To']
    print('Ok')
"""
'''