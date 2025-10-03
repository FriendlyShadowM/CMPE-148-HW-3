from socket import *
import time

# Free SMTP testing services to try
SMTP_SERVERS = [
    ("smtp.freesmtpservers.com", 25),
    ("smtp.ethereal.email", 587),  # Ethereal Email testing service
    ("localhost", 1025),  # Local testing server
]

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

def try_smtp_server(mailserver, port):
    """Try to connect and send email via SMTP server"""
    try:
        print(f"\n=== Trying SMTP server: {mailserver}:{port} ===")
        
        # Create socket called clientSocket and establish a TCP connection with mailserver
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.settimeout(10)  # 10 second timeout
        clientSocket.connect((mailserver, port))
        print(f"✅ Connected to {mailserver}:{port}")
        
        recv = clientSocket.recv(1024).decode()
        print(f"Server greeting: {recv.strip()}")
        if recv[:3] != '220':
            print('220 reply not received from server.')
            clientSocket.close()
            return False

        # Send HELO command and print server response.
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        print(f"HELO response: {recv1.strip()}")
        if recv1[:3] != '250':
            print('250 reply not received from server.')
            clientSocket.close()
            return False

        # Send MAIL FROM command and print server response.
        mailFromCommand = 'MAIL FROM:<test.sender@example.com>\r\n'
        clientSocket.send(mailFromCommand.encode())
        recv2 = clientSocket.recv(1024).decode()
        print(f"MAIL FROM response: {recv2.strip()}")
        if recv2[:3] != '250':
            print('250 reply not received from server.')
            clientSocket.close()
            return False

        # Send RCPT TO command and print server response.
        rcptToCommand = 'RCPT TO:<test.recipient@example.com>\r\n'
        clientSocket.send(rcptToCommand.encode())
        recv3 = clientSocket.recv(1024).decode()
        print(f"RCPT TO response: {recv3.strip()}")
        if recv3[:3] != '250':
            print('250 reply not received from server.')
            clientSocket.close()
            return False

        # Send DATA command and print server response.
        dataCommand = 'DATA\r\n'
        clientSocket.send(dataCommand.encode())
        recv4 = clientSocket.recv(1024).decode()
        print(f"DATA response: {recv4.strip()}")
        if recv4[:3] != '354':
            print('354 reply not received from server.')
            clientSocket.close()
            return False

        # Send message data.
        subject = "Subject: Test email from SMTP client\r\n\r\n"
        clientSocket.send(subject.encode())
        clientSocket.send(msg.encode())

        # Message ends with a single period.
        clientSocket.send(endmsg.encode())
        recv5 = clientSocket.recv(1024).decode()
        print(f"Message response: {recv5.strip()}")
        if recv5[:3] != '250':
            print('250 reply not received from server.')
            clientSocket.close()
            return False

        # Send QUIT command and get server response.
        quitCommand = 'QUIT\r\n'
        clientSocket.send(quitCommand.encode())
        recv6 = clientSocket.recv(1024).decode()
        print(f"QUIT response: {recv6.strip()}")
        clientSocket.close()
        
        print(f"✅ Email sent successfully via {mailserver}:{port}!")
        return True
        
    except Exception as e:
        print(f"❌ Error with {mailserver}:{port}: {e}")
        return False

def main():
    print("=== SMTP Client - Multiple Server Test ===")
    print("Testing various SMTP servers for email sending...\n")
    
    success = False
    for mailserver, port in SMTP_SERVERS:
        if try_smtp_server(mailserver, port):
            success = True
            break
        time.sleep(1)  # Brief pause between attempts
    
    if not success:
        print("\n❌ No SMTP servers were accessible.")
        print("\nALTERNATIVE OPTIONS:")
        print("1. Use Gmail with smtp_client_tls.py (most reliable)")
        print("2. Try your university's SMTP server")
        print("3. Set up a local SMTP testing server")
        print("4. Use online SMTP testing tools")
        
        print("\nFor demonstration purposes, here's what the successful output looks like:")
        print("="*60)
        print("Server greeting: 220 smtp.example.com ESMTP ready")
        print("HELO response: 250 smtp.example.com Hello Alice")
        print("MAIL FROM response: 250 OK")
        print("RCPT TO response: 250 OK")
        print("DATA response: 354 Send message data; end with <CRLF>.<CRLF>")
        print("Message response: 250 OK Message accepted")
        print("QUIT response: 221 Bye")
        print("✅ Email sent successfully!")
        print("="*60)

if __name__ == "__main__":
    main()