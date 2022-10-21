import smtplib, ssl
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


port = 465 # For SSL
# port  = 587 # For starttls
sender_email = input("Enter sender_email: ")
receiver_email = input("Enter receiver_email: ")
password = getpass.getpass("Enter the password: ")


message = MIMEMultipart()
message['Subject'] = input("Mail's Subject: ")
message['From'] = sender_email
message['To'] = receiver_email
content = input("Your message:\n")
text = MIMEText(content, "plain")
message.attach(text)


# Secure SSL context
ctx = ssl.create_default_context()


# SMTP_SSL()

# Secure a connection with the server
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=ctx) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )


# starttls()
# try:
#     server = smtplib.SMTP("smtp.gmail.com", port)
#     server.starttls(context=ctx)
#     server.login(sender_email, password)
#     print(server.ehlo())


# except Exception as e:
#     print(e)

# finally:
#     server.close()
