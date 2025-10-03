from socket import *
import ssl
import base64
import mimetypes
import os

# Configuration
GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"  # Replace with your Gmail address
SENDER_PASSWORD = "your_app_password"  # Replace with your Gmail app password
RECIPIENT_EMAIL = "recipient@example.com"  # Replace with recipient's email

def encode_file_in_base64(file_path):
    """Encode a file in base64 for email attachment."""
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

def get_content_type(file_path):
    """Get the MIME content type of a file."""
    content_type, _ = mimetypes.guess_type(file_path)
    return content_type or 'application/octet-stream'

def create_multipart_message(text_content, image_path=None):
    """Create a multipart email message with text and optional image."""
    boundary = "----=_NextPart_000_001_01D0A1B2.3C4D5E6F"
    
    # Email headers
    message = f"MIME-Version: 1.0\r\n"
    message += f"Content-Type: multipart/mixed; boundary=\"{boundary}\"\r\n\r\n"
    
    # Text part
    message += f"--{boundary}\r\n"
    message += "Content-Type: text/plain; charset=utf-8\r\n"
    message += "Content-Transfer-Encoding: 7bit\r\n\r\n"
    message += text_content + "\r\n\r\n"
    
    # Image attachment (if provided)
    if image_path and os.path.exists(image_path):
        filename = os.path.basename(image_path)
        content_type = get_content_type(image_path)
        encoded_image = encode_file_in_base64(image_path)
        
        message += f"--{boundary}\r\n"
        message += f"Content-Type: {content_type}; name=\"{filename}\"\r\n"
        message += "Content-Transfer-Encoding: base64\r\n"
        message += f"Content-Disposition: attachment; filename=\"{filename}\"\r\n\r\n"
        
        # Split base64 string into 76-character lines (RFC requirement)
        for i in range(0, len(encoded_image), 76):
            message += encoded_image[i:i+76] + "\r\n"
        message += "\r\n"
    
    # End boundary
    message += f"--{boundary}--\r\n"
    
    return message

# Message content
text_msg = "I love computer networks!\n\nThis email was sent using a custom SMTP client with attachment support."
image_path = "sample_image.jpg"  # Replace with actual image path or set to None

# End message marker
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = GMAIL_SMTP_SERVER  # Fill in start   #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, GMAIL_SMTP_PORT))
# Fill in end

recv = clientSocket.recv(1024).decode()
print("Server response:", recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("HELO response:", recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Start TLS (required for Gmail)
# Fill in start
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv_tls = clientSocket.recv(1024).decode()
print("STARTTLS response:", recv_tls)
if recv_tls[:3] != '220':
    print('220 reply not received for STARTTLS.')

# Wrap socket with SSL
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Send HELO again after TLS
clientSocket.send(heloCommand.encode())
recv1_tls = clientSocket.recv(1024).decode()
print("HELO after TLS response:", recv1_tls)
# Fill in end

# Authenticate with Gmail (using LOGIN method)
# Fill in start
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv_auth = clientSocket.recv(1024).decode()
print("AUTH LOGIN response:", recv_auth)

# Send username (base64 encoded)
username_b64 = base64.b64encode(SENDER_EMAIL.encode()).decode()
clientSocket.send((username_b64 + '\r\n').encode())
recv_user = clientSocket.recv(1024).decode()
print("Username response:", recv_user)

# Send password (base64 encoded)
password_b64 = base64.b64encode(SENDER_PASSWORD.encode()).decode()
clientSocket.send((password_b64 + '\r\n').encode())
recv_pass = clientSocket.recv(1024).decode()
print("Password response:", recv_pass)
if recv_pass[:3] != '235':
    print('Authentication failed.')
# Fill in end

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = f'MAIL FROM:<{SENDER_EMAIL}>\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print("MAIL FROM response:", recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = f'RCPT TO:<{RECIPIENT_EMAIL}>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print("RCPT TO response:", recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print("DATA response:", recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data with attachments.
# Fill in start
email_headers = f"From: {SENDER_EMAIL}\r\n"
email_headers += f"To: {RECIPIENT_EMAIL}\r\n"
email_headers += "Subject: Test email with text and image attachment\r\n"

# Create multipart message
multipart_message = create_multipart_message(text_msg, image_path if os.path.exists(image_path) else None)

# Send headers and message
full_message = email_headers + multipart_message
clientSocket.send(full_message.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print("Message sent response:", recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print("QUIT response:", recv6)
clientSocket.close()
print("Email with attachment sent successfully!")
# Fill in end