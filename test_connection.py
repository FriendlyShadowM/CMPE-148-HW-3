import socket

def test_smtp_connection(server, port):
    """Test if we can connect to an SMTP server"""
    try:
        print(f"Testing connection to {server}:{port}...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # 10 second timeout
        result = sock.connect_ex((server, port))
        
        if result == 0:
            print(f"✅ Connection successful to {server}:{port}")
            
            # Try to receive the greeting
            try:
                sock.settimeout(5)
                greeting = sock.recv(1024).decode()
                print(f"Server greeting: {greeting.strip()}")
            except Exception as e:
                print(f"Could not read greeting: {e}")
            
            sock.close()
            return True
        else:
            print(f"❌ Connection failed to {server}:{port}")
            return False
            
    except Exception as e:
        print(f"❌ Error connecting to {server}:{port}: {e}")
        return False

if __name__ == "__main__":
    print("=== SMTP Server Connectivity Test ===\n")
    
    # Test various SMTP servers
    servers = [
        ("smtp.freesmtpservers.com", 25),
        ("smtp.gmail.com", 587),
        ("smtp.gmail.com", 25),
        ("smtp.outlook.com", 587),
    ]
    
    for server, port in servers:
        test_smtp_connection(server, port)
        print()