"""
Gmail SMTP Setup Guide
======================

IMPORTANT: Before running smtp_client_tls.py, you MUST set up Gmail App Password:

Step 1: Enable 2-Factor Authentication
--------------------------------------
1. Go to https://myaccount.google.com
2. Click "Security" in the left sidebar
3. Under "How you sign in to Google", click "2-Step Verification"
4. Follow the setup process if not already enabled

Step 2: Generate App Password
-----------------------------
1. Go back to Security settings
2. Under "2-Step Verification", click "App passwords"
3. Select "Mail" from the dropdown
4. Click "Generate"
5. Copy the 16-character password (format: abcd efgh ijkl mnop)

Step 3: Update smtp_client_tls.py
----------------------------------
Replace these lines in smtp_client_tls.py:

SENDER_EMAIL = "your_actual_email@gmail.com"      # Your real Gmail address
SENDER_PASSWORD = "your_16_char_app_password"     # The app password from step 2
RECIPIENT_EMAIL = "recipient@example.com"         # Where to send the test email

Example:
SENDER_EMAIL = "john.doe@gmail.com"
SENDER_PASSWORD = "abcd efgh ijkl mnop"           # Remove spaces when entering
RECIPIENT_EMAIL = "friend@example.com"

Step 4: Run the Program
-----------------------
python smtp_client_tls.py

Expected Success Output:
------------------------
Server response: 220 smtp.gmail.com ESMTP...
HELO response: 250 smtp.gmail.com at your service
STARTTLS response: 220 2.0.0 Ready to start TLS
HELO after TLS response: 250 smtp.gmail.com at your service
AUTH LOGIN response: 334 VXNlcm5hbWU6
Username response: 334 UGFzc3dvcmQ6
Password response: 235 2.7.0 Accepted          <-- This should say "Accepted"
MAIL FROM response: 250 2.1.0 OK
RCPT TO response: 250 2.1.5 OK
DATA response: 354 Go ahead
Message sent response: 250 2.0.0 OK
QUIT response: 221 2.0.0 closing connection
Email sent successfully!

Step 5: Check Email
-------------------
Check the recipient's inbox (and spam folder) for the test email.

Common Issues:
--------------
- "Username and Password not accepted" = Wrong credentials or no App Password
- "Authentication Required" = Need to complete authentication first
- "Must issue STARTTLS" = Using wrong version (use smtp_client_tls.py, not smtp_client.py)

Security Notes:
---------------
- Never commit real passwords to git
- Use App Passwords, not your main Gmail password
- The App Password is specific to this application
"""

print(__doc__)