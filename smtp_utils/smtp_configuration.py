"""
SMTP configuration utility for sending emails via SMTP.

Loads SMTP settings from environment variables (.env file)
and sends an email securely using TLS.
"""

import os
import smtplib
import logging
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


def smtp_configurations(to_email: str, subject: str, body: str) -> bool:
    """
    Send an email via configured SMTP server.

    Args:
        to_email (str): Recipient email address.
        subject (str): Subject line of the email.
        body (str): Email message body (plain text).

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USERNAME
        msg["To"] = to_email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, to_email, msg.as_string())

        logging.info(f"✅ Email sent to {to_email} with subject '{subject}'")
        return True

    except Exception as e:
        logging.error(f"❌ Failed to send email to {to_email}: {e}")
        return False
