import smtplib
from email.message import EmailMessage

def send_mail(to,text):
    sender = 'shirblog2@gmail.com'
    pswd = ''
    servername = 'smtp.gmail.com'
    
    server = smtplib.SMTP(servername, 587)
    server.starttls()
    
    msg = EmailMessage()
    msg['Subject'] = f'Warning!!!'
    msg['From'] = sender
    msg['To'] = to
    msg.set_content(text)
    
    
    server.login(sender,pswd)
    server.send_message(msg)