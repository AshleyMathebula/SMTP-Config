"""
Example: Using smtp_configurations() to send an email.

Before running:
1. Create a .env file (see .env.example).
2. Install dependencies: pip install -r requirements.txt
3. Run this file: python example_send.py
"""

from smtp_utils.smtp_configurations import smtp_configurations

if __name__ == "__main__":
    to_email = "recipient@example.com"
    subject = "SMTP Config Test Email"
    body = (
        "Hi there,\n\n"
        "This is a test email sent using the smtp_configurations() function.\n"
        "If you received this, your setup works correctly.\n\n"
        "Best,\n"
        "SMTP Config Utility"
    )

    success = smtp_configurations(to_email, subject, body)

    if success:
        print(f"✅ Email successfully sent to {to_email}")
    else:
        print(f"❌ Failed to send email to {to_email}")
