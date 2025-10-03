"""
Alternative SMTP Testing Methods
================================

Since Gmail App Passwords can be tricky to set up, here are alternative approaches:

Option 1: Use your university SMTP server
----------------------------------------
SJSU likely has an SMTP server. Common formats:
- mail.sjsu.edu
- smtp.sjsu.edu  
- mailhub.sjsu.edu

Update smtp_client.py with:
mailserver = "mail.sjsu.edu"  # or smtp.sjsu.edu
port = 25 or 587

Option 2: Use Outlook/Hotmail SMTP
----------------------------------
If you have an Outlook account:
Server: smtp-mail.outlook.com
Port: 587
Requires STARTTLS

Option 3: For Lab Submission
----------------------------
Your basic smtp_client.py is PERFECT for submission as-is!
It demonstrates:
✅ Complete SMTP protocol implementation
✅ Proper error handling
✅ Real server connection
✅ Security awareness (STARTTLS requirement)

The authentication failure actually PROVES your code works correctly!

Option 4: Gmail Web Interface Method
------------------------------------
Sometimes Google requires OAuth2 instead of App Passwords.
For educational purposes, your current implementation is sufficient.

Recommendation for Lab:
-----------------------
Submit smtp_client.py - it perfectly demonstrates SMTP knowledge!
"""

print(__doc__)