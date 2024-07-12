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
<<<<<<< Updated upstream:send_emails.py
    body = """
Hello George,

This is a test email containing the qr code for the first guest in the database (really just my csv file).
Basically, it is a function called send_email that takes in the sender's email, the sender's password, the recipient's email, the subject of the email, the body of the email, and the image to attach to the email.
The credentials for my test email are as follows:
email: bigbarrold.dev@gmail.com
password: hgcq wzzf hsoj baxm

In the final project, this can be called at the end of the loop that generates the uuids and qr codes for each guest in the database. Pass in the email of the guest as the recipient and the qr code image as the attachment.
Anyway, I have spent way too much time trying to get this to work, so I'm just going to update my branch of the project and assume all is well.
"""
    image = "guest0.png"
=======
    body = "Hello, this is Python. I am sending you an email with an attachment please scan."

    image = "/Documents/Code/Python/BT_event/rickroll.png"
>>>>>>> Stashed changes:qrcodes/send_emails.py

    recipients = ["icallumbird@icloud.com"]

    # tests by sending the email to members of the BT group
    for recipient in recipients:
        send_email(email_sender, email_password, recipient, subject, body, image)
