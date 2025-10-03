from socket import *
import ssl
import base64

# Configuration
GMAIL_SMTP_SERVER = "smtp.gmail.com"  # Change back to Gmail
GMAIL_SMTP_PORT = 587  # Change back to Gmail port
SENDER_EMAIL = "testCMPE148@gmail.com"  # Replace with your Gmail address
SENDER_PASSWORD = "your_16_char_app_password_here"  # Replace with Gmail App Password (16 chars)
RECIPIENT_EMAIL = "marcus.vu@sjsu.edu"  # Replace with recipient's email

msg = "\r\n I love computer networks!"
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
    print('❌ Authentication failed! Please check your Gmail App Password setup.')
    print('Run: python gmail_setup_guide.py for setup instructions')
    clientSocket.close()
    exit(1)
print("✅ Authentication successful!")
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

# Send message data.
# Fill in start
email_headers = f"From: {SENDER_EMAIL}\r\n"
email_headers += f"To: {RECIPIENT_EMAIL}\r\n"
email_headers += "Subject: Test email from SMTP client with TLS\r\n\r\n"
clientSocket.send(email_headers.encode())
clientSocket.send(msg.encode())
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
print("Email sent successfully!")
# Fill in end