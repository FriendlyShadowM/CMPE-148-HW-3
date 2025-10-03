# SMTP Client Configuration Template
# Copy this file to config.py and update with your actual values

# Gmail SMTP Configuration
GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

# Email Credentials (replace with your actual values)
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_16_character_app_password"  # Gmail App Password
RECIPIENT_EMAIL = "recipient@example.com"

# Alternative Mail Servers (for testing)
# University mail server example:
# UNIVERSITY_SMTP_SERVER = "mail.university.edu"
# UNIVERSITY_SMTP_PORT = 25

# AOL mail server example:
# AOL_SMTP_SERVER = "smtp.aol.com"
# AOL_SMTP_PORT = 587

# Message Configuration
DEFAULT_SUBJECT = "Test email from SMTP client"
DEFAULT_MESSAGE = "I love computer networks!"

# File paths for attachments (optional)
SAMPLE_IMAGE_PATH = "sample_image.jpg"