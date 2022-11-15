import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_emails(list_of_receivers, metric, value, average):
    port = 465  # For SSL
    password = os.getenv("EMAIL_PASS")
    sender_email = os.getenv("SENDER_EMAIL")

    context = ssl.create_default_context()

    for receiver_email in list_of_receivers:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            if True:
                message = MIMEMultipart("alternative")
                message["Subject"] = f"ALERT - rychlost {metric}"
                message["From"] = sender_email
                message["To"] = receiver_email
                text = f"""\
                Rychlost metriky {metric} stoupla oproti průměru za posledních 5 dní.
                Aktuální hodnota je {value} a průměr je {average}"""

                html = f"""\
                <html>
                  <body>
                    <p>Rychlost metriky {metric} stoupla oproti průměru za posledních 5 dní.
                        Aktuální hodnota je {value} a průměr je {average}
                    </p>
                  </body>
                </html>
                """

                # Turn these into plain/html MIMEText objects
                part1 = MIMEText(text, "plain")
                part2 = MIMEText(html, "html")

                # Add HTML/plain-text parts to MIMEMultipart message
                # The email client will try to render the last part first
                message.attach(part1)
                message.attach(part2)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
