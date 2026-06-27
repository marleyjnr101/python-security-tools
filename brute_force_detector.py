import sys
ips = []
count = []

filename = sys.argv[1]
with open(filename,"r") as f:
  for line in f:
    line = line.strip()
    parts = line.split()
    ip = parts[0]
    if ip  not in  ips:
      ips.append(ip)
      count.append(1)
    else  :
      position = ips.index(ip)
      count[position] =+ 1
    threat = len(ip) >= 3
    print(threat)
    print(f"total threats detected :{count}")
          
      
      
        
    
    