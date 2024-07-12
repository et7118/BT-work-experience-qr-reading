# email test
from email.message import EmailMessage
import ssl  # for secure connection to protect sensitive information
import smtplib  # for sending the email

def send_email(email_sender: str, email_password: str, email_recipient: str, subject: str, body: str, attachment: str) -> None:

    # create an email message object
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_recipient
    em["Subject"] = subject
    em.set_content(body)

    # attach the file
    with open(attachment, "rb") as file:
        em.add_attachment(file.read(), maintype="application", subtype="octet-stream", filename=file.name)

    context = ssl.create_default_context()  # create a secure connection

    # send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_password)
        server.send_message(em)
        print("Email sent successfully")


if __name__ == "__main__":

    # sender credentials
    email_sender = "bigbarrold.dev@gmail.com"
    email_password = "hgcq wzzf hsoj baxm"

    # email content
    subject = "QR Code Test Email"

    # using tripple quotes to make a multi-line string - apparently that is a thing in Python
    body = "Hello from Python!"
    image = "guest0.png"

    recipients = ["icallumbird@icloud.com"]

    # tests by sending the email to members of the BT group
    for recipient in recipients:
        send_email(email_sender, email_password, recipient, subject, body, image)
