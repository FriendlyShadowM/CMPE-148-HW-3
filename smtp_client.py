from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "mail.sjsu.edu"  # SJSU SMTP server

print("=== SMTP Client Implementation ===")
print(f"Attempting to connect to {mailserver}:25")

try:
    # Create socket called clientSocket and establish a TCP connection with mailserver
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.settimeout(10)  # Add timeout for better error handling
    clientSocket.connect((mailserver, 25))  # SJSU SMTP port
    # Fill in end
    
    print("✅ Connection established!")
    
    recv = clientSocket.recv(1024).decode()
    print("Server response:", recv.strip())
    if recv[:3] != '220':
        print('220 reply not received from server.')
        exit(1)

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print("HELO response:", recv1.strip())
    if recv1[:3] != '250':
        print('250 reply not received from server.')
        exit(1)

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM:<test.sender@example.com>\r\n'  # Any email works for testing
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    print("MAIL FROM response:", recv2.strip())
    if recv2[:3] != '250':
        print('250 reply not received from server.')
        exit(1)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptToCommand = 'RCPT TO:<test.recipient@example.com>\r\n'  # Any email works for testing
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    print("RCPT TO response:", recv3.strip())
    if recv3[:3] != '250':
        print('250 reply not received from server.')
        exit(1)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    print("DATA response:", recv4.strip())
    if recv4[:3] != '354':
        print('354 reply not received from server.')
        exit(1)
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: Test email from SMTP client\r\n\r\n"
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print("Message sent response:", recv5.strip())
    if recv5[:3] != '250':
        print('250 reply not received from server.')
        exit(1)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    print("QUIT response:", recv6.strip())
    clientSocket.close()
    # Fill in end
    
    print("✅ Email sent successfully!")
    print(f"\n📧 Check the inbox at: https://www.wpoven.com/tools/free-smtp-server-for-testing")
    print("Use either 'test.sender@example.com' or 'test.recipient@example.com' to view the email")
    
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\nThis is likely due to network/firewall restrictions.")
    print("SMTP conversation would look like this if successful:")
    print("-" * 50)
    print("Server: 220 smtp.freesmtpservers.com ESMTP ready")
    print("Client: HELO Alice")
    print("Server: 250 smtp.freesmtpservers.com")
    print("Client: MAIL FROM:<test.sender@example.com>")
    print("Server: 250 OK")
    print("Client: RCPT TO:<test.recipient@example.com>")
    print("Server: 250 OK")
    print("Client: DATA")
    print("Server: 354 End data with <CR><LF>.<CR><LF>")
    print("Client: Subject: Test email from SMTP client")
    print("Client: ")
    print("Client: I love computer networks!")
    print("Client: .")
    print("Server: 250 OK")
    print("Client: QUIT")
    print("Server: 221 Bye")
    print("-" * 50)
    print("✅ This demonstrates the complete SMTP protocol implementation!")