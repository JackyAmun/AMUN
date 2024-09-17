import smtplib  
import imaplib  
import email  
from email.mime.text import MIMEText  
import getpass  
import os  
import datetime
from email.mime.multipart import MIMEMultipart  
from email.header import decode_header
import sys
import subprocess 

def show_menu():  
    print("1. Time")  
    print("2. Find")  
    print("3. Send Email")  
    print("4. Receive Email")
    print("5. Amun explorer")
    print("6. Calculator")
    print("7. Paint")
    print("8. Picture viewer")
    print("9. go back")
    choice = input("Enter your choice (1-5): ")  
    return choice  
  
def show_time():  
    print("Current time:", datetime.datetime.now())
    show_menu()  
  
def find_in_computer():  
    try:    
        root_dir = input("Enter the root directory to start the search (e.g., C:\\): ")  
        search_term = input("Enter the filename or foldername (or partial name) to find: ")  
        search_type = input("Search for [F]ile, [D]irectory, or [B]oth? ").lower()  
        found = False    
        for root, dirs, files in os.walk(root_dir):    
            if search_type in ['f', 'b']:  
                for file in files:  
                    if search_term in file:  
                        print(f"File found: {os.path.join(root, file)}")  
                        found = True    
            if search_type in ['d', 'b']:  
                for dir_name in dirs:  
                    if search_term in dir_name:  
                        print(f"Directory found: {os.path.join(root, dir_name)}")  
                        found = True  
  
            # 如果在找到文件或文件夹后想立即退出整个搜索，可以取消下面if语句的注释  
            # 并注释掉上面两个循环中的break语句（如果存在）  
            # if found:  
            #     break  # 如果你想在找到第一个匹配的文件或文件夹后就退出整个搜索  
  
        if not found:  
            print(f"No files or directories matching '{search_term}' found in {root_dir} or its subdirectories.")  
  
    except Exception as e:  
        print(f"An error occurred during the search: {e}")
        show_menu()

def send_email():  
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
        show_menu()
    except Exception as e:  
        # 如果发送过程中出现异常，打印错误信息  
        print(f"Failed to send email: {e}")

def receive_email():  
    try:  
        imap_server = input("Enter IMAP server: ")  
        email_address = input("Enter your email: ")  
        password = getpass.getpass("Enter your email password: ")  
  
        mail = imaplib.IMAP4_SSL(imap_server)  
        mail.login(email_address, password)  
        mail.select('inbox')  
  
        _, search_data = mail.search(None, 'ALL')  
        if search_data[0] == '':  
            print("No emails found.")  
            return  
  
        for num in search_data[0].split():  
            _, msg_data = mail.fetch(num.decode('utf-8'), '(RFC822)')  
            _, msg_bytes = msg_data[0]  
            msg = email.message_from_bytes(msg_bytes)  
            print(f"Email {num.decode('utf-8')}: From {msg['From']} - Subject {msg['Subject']}")  
  
        mail.close()  
        mail.logout()  
    except Exception as e:  
        print(f"Failed to receive emails: {e}")
        show_menu()
        
def main():  
    try:  
        choice = show_menu()  
        if choice == '1':  
            show_time()  
        elif choice == '2':  
            find_in_computer()
        elif choice == '3':  
            send_email()  
        elif choice == '4':  
            receive_email()
        elif choice == '5':
            subprocess.run(["python", "App\\Amun explorer.py"])
        elif choice == '6':
            subprocess.run(["python", "App\\calculator.py"])
        elif choice == '7':
            subprocess.run(["python", "App\\paint.py"])
        elif choice == '8':
            subprocess.run(["python", "App\\Picture viewer.py"])
        elif choice == '9':
            sys.exit()
        else:  
            print("Invalid choice, please try again.")  
    except KeyboardInterrupt:  
        print("\nProgram interrupted by user.")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  
  
if __name__ == "__main__":  
    main()
