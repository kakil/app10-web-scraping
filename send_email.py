import smtplib, ssl
import os
import dotenv

dotenv.load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("GOOGLE_USERNAME")
    password = os.getenv("GOOGLE_APP_PASSWORD")

    receiver = os.getenv("GOOGLE_USERNAME")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
