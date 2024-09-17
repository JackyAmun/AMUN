import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
  
sender_email = input("Sender Email: ")    
smtp_server = input("SMTP server: ")    
smtp_port = int(input("SMTP port: "))    
password = input("Sender password: ")    
subject = input("Email subject: ")    
content = input("Email content: ")    
recipient = input("Recipient Email: ")    
    
# 创建SMTP对象    
try:    
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)    
    smtp_obj.starttls()  # 启用TLS加密    
    
    # 登录到发件人邮箱    
    smtp_obj.login(sender_email, password)    
    
    # 创建邮件对象    
    msg = MIMEMultipart()    
    msg['From'] = sender_email    
    msg['To'] = recipient    
    msg['Subject'] = subject    
    body = content    
    msg.attach(MIMEText(body, 'plain'))    
    
    # 发送邮件    
    smtp_obj.send_message(msg)    
    smtp_obj.quit()    
    
    # 在控制台显示成功信息    
    print("Email sent successfully!")    
except Exception as e:    
    # 如果发送过程中出现异常，打印错误信息    
    print(f"Failed to send email: {e}")
