"""
SMTP Client Usage Examples and Testing Guide

This file demonstrates how to test and use the SMTP clients.
"""

def test_basic_smtp():
    """Test the basic SMTP client (smtp_client.py)"""
    print("Testing Basic SMTP Client:")
    print("1. Update mailserver variable in smtp_client.py")
    print("2. Update sender and recipient email addresses")
    print("3. Run: python smtp_client.py")
    print("Note: May not work with Gmail due to security requirements\n")

def test_tls_smtp():
    """Test the TLS SMTP client (smtp_client_tls.py)"""
    print("Testing TLS SMTP Client:")
    print("1. Set up Gmail App Password")
    print("2. Update SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL")
    print("3. Run: python smtp_client_tls.py")
    print("4. Check recipient's inbox (and spam folder)")
    print("Expected: Email with subject 'Test email from SMTP client with TLS'\n")

def test_attachment_smtp():
    """Test the attachment SMTP client (smtp_client_with_attachments.py)"""
    print("Testing SMTP Client with Attachments:")
    print("1. Same Gmail setup as TLS client")
    print("2. Place an image file in the directory (e.g., sample_image.jpg)")
    print("3. Update image_path variable if needed")
    print("4. Run: python smtp_client_with_attachments.py")
    print("5. Check recipient's inbox for email with attachment")
    print("Expected: Email with text and image attachment\n")

def gmail_setup_guide():
    """Guide for setting up Gmail App Password"""
    print("Gmail App Password Setup:")
    print("1. Go to your Google Account (myaccount.google.com)")
    print("2. Navigate to Security")
    print("3. Enable 2-Step Verification if not already enabled")
    print("4. Under 2-Step Verification, click 'App passwords'")
    print("5. Select 'Mail' as the app")
    print("6. Copy the 16-character password")
    print("7. Use this password in SENDER_PASSWORD variable")
    print("8. Never use your regular Gmail password for SMTP\n")

def troubleshooting():
    """Common troubleshooting tips"""
    print("Troubleshooting Tips:")
    print("- Check spam/junk folder for received emails")
    print("- Ensure 2FA is enabled on Gmail before creating App Password")
    print("- Verify email addresses are correctly formatted")
    print("- Some networks may block SMTP ports (try different networks)")
    print("- University mail servers may have different requirements")
    print("- Use telnet to test SMTP server connectivity:")
    print("  telnet smtp.gmail.com 587")
    print("- Check firewall settings if connection fails\n")

def expected_output():
    """Show expected console output"""
    print("Expected Console Output (TLS version):")
    print("Server response: 220 smtp.gmail.com ESMTP...")
    print("HELO response: 250 smtp.gmail.com at your service...")
    print("STARTTLS response: 220 2.0.0 Ready to start TLS")
    print("HELO after TLS response: 250 smtp.gmail.com at your service...")
    print("AUTH LOGIN response: 334 VXNlcm5hbWU6")
    print("Username response: 334 UGFzc3dvcmQ6")
    print("Password response: 235 2.7.0 Accepted")
    print("MAIL FROM response: 250 2.1.0 OK...")
    print("RCPT TO response: 250 2.1.5 OK...")
    print("DATA response: 354 Go ahead...")
    print("Message sent response: 250 2.0.0 OK...")
    print("QUIT response: 221 2.0.0 closing connection...")
    print("Email sent successfully!")

if __name__ == "__main__":
    print("=== SMTP Client Testing Guide ===\n")
    test_basic_smtp()
    test_tls_smtp()
    test_attachment_smtp()
    gmail_setup_guide()
    troubleshooting()
    expected_output()