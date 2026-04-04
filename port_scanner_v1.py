import socket

target = "10.0.2.3"
ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 161]
for port in ports_to_scan:
   
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
                print(f"port {port}: OPEN - Banner: {banner}")
            except:
                print(f"port {port}: OPEN - No banner")
                s.close()
        else:
            print(f"port {port}: CLOSED")
    except Exception as e:
                print(f"port {port}: Error - {e}")
    
