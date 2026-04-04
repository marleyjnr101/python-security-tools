import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python port_scanner.py <IP> <port_range>")
    print("Example: python port_scanner.py 10.0.2.3 1-1024")
    sys.exit(1)

target = sys.argv[1]
port_range = sys.argv[2].split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
                print(f"Port {port}: OPEN — {banner}")
            except:
                print(f"Port {port}: OPEN")
        s.close()
    except:
        pass