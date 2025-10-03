# CMPE-148-HW-3: SMTP Lab Implementation

This repository contains the implementation of a simple SMTP mail client for CMPE 148 Lab 3. The client demonstrates how to send emails using raw socket programming and the SMTP protocol without using Python's built-in `smtplib` module.

## Files Overview

1. **`smtp_client.py`** - Basic SMTP client implementation (skeleton code completed)
2. **`smtp_client_tls.py`** - Enhanced version with TLS/SSL support for Gmail
3. **`smtp_client_with_attachments.py`** - Advanced version supporting both text and image attachments

## Basic SMTP Client (`smtp_client.py`)

This is the completed skeleton code that demonstrates the basic SMTP protocol flow:

### Features:
- TCP socket connection to SMTP server
- Basic SMTP commands: HELO, MAIL FROM, RCPT TO, DATA, QUIT
- Error checking for server responses
- Simple text message sending

### Usage:
```python
# Modify these variables before running:
mailserver = "smtp.gmail.com"  # Change to your preferred mail server
# Update email addresses in MAIL FROM and RCPT TO commands
```

## TLS/SSL Enhanced Client (`smtp_client_tls.py`)

This version includes TLS/SSL support required by modern mail servers like Gmail.

### Features:
- All features from basic client
- STARTTLS command for secure connection
- SSL context wrapping
- LOGIN authentication with base64 encoding
- Compatible with Gmail SMTP server (smtp.gmail.com:587)

### Setup for Gmail:
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. Update the configuration variables:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   SENDER_PASSWORD = "your_16_character_app_password"
   RECIPIENT_EMAIL = "recipient@example.com"
   ```

### Usage:
```bash
python smtp_client_tls.py
```

## Advanced Client with Attachments (`smtp_client_with_attachments.py`)

This version supports sending emails with both text content and image attachments.

### Features:
- All features from TLS client
- MIME multipart message support
- Base64 encoding for file attachments
- Automatic content type detection
- Support for various image formats

### Setup:
1. Same Gmail setup as TLS client
2. Place an image file in the same directory or update the `image_path` variable
3. Run the script:
   ```bash
   python smtp_client_with_attachments.py
   ```

## SMTP Protocol Flow

All implementations follow this SMTP protocol sequence:

1. **Connect** - Establish TCP connection to SMTP server
2. **HELO** - Identify client to server
3. **STARTTLS** - (TLS versions only) Initiate secure connection
4. **AUTH LOGIN** - (Secure versions only) Authenticate with credentials
5. **MAIL FROM** - Specify sender email address
6. **RCPT TO** - Specify recipient email address
7. **DATA** - Begin message transmission
8. **Message Content** - Send email headers and body
9. **End Data** - Signal end of message with "\\r\\n.\\r\\n"
10. **QUIT** - Close connection

## Server Response Codes

- **220** - Service ready
- **250** - Requested action completed successfully
- **354** - Start mail input (response to DATA command)
- **235** - Authentication successful

## Testing Notes

- Some mail servers may classify emails as spam/junk
- Check spam folder if emails don't appear in inbox
- Gmail requires App Passwords when 2FA is enabled
- Some mail servers may block connections from certain IP ranges

## Lab Requirements Fulfilled

✅ Complete skeleton code implementation  
✅ Socket programming without using `smtplib`  
✅ SMTP protocol dialogue with mail server  
✅ Error checking and server response validation  
✅ Optional Exercise 1: TLS/SSL support for Gmail  
✅ Optional Exercise 2: Text and image attachment support  

## Screenshots

To complete the lab submission, take screenshots showing:
1. Successful execution of the SMTP client
2. Received email in the recipient's inbox
3. Email content displaying "I love computer networks!"

## Security Notes

- Never commit real email credentials to version control
- Use App Passwords instead of your main Gmail password
- Consider using environment variables for sensitive configuration
- Test with university mail servers as an alternative to Gmail