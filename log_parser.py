import sys 
filename = sys.argv[1]
total_404 = 0
attacking_ip = []

with open(filename,"r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 4 :
            ip = parts[0]
            status = parts[-1]    
            if status == "404":
                total_404 += 1   
            if ip  not in attacking_ip:
                attacking_ip.append(ip) 
                
print(f"Total 404: {total_404}")                
print(f"Unique attackers : {len(attacking_ip)}")
for ip in attacking_ip :
    print(f"  {ip}")