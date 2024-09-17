import imaplib
from email.mime.multipart import MIMEMultipart  
from email.header import decode_header
import email

try:  
    imap_server = input("Enter IMAP server: ")  
    email_address = input("Enter your email: ")  
    password = input("Enter your email password: ")  
  
    mail = imaplib.IMAP4_SSL(imap_server)  
    mail.login(email_address, password)  
    mail.select('inbox')  
  
    _, search_data = mail.search(None, 'ALL')  
    if search_data[0] == '':  
        print("No emails found.")   
  
    for num in search_data[0].split():  
        _, msg_data = mail.fetch(num.decode('utf-8'), '(RFC822)')  
        _, msg_bytes = msg_data[0]  
        msg = email.message_from_bytes(msg_bytes)  
        print(f"Email {num.decode('utf-8')}: From {msg['From']} - Subject {msg['Subject']}")  
  
    mail.close()  
    mail.logout()  
except Exception as e:  
    print(f"Failed to receive emails: {e}")
