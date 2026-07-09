ip_numbers = [1, 6, 17, 2]
parsed_protocols = []
for num in ip_numbers:
    if num == 1:
        s_name = "ICMP"
    elif num == 6:
        s_name = "TCP"    
    elif num == 17:
        s_name = "UDP"
    else:
        s_name = "other"
     
    update = f"Protocol {num}: {s_name}"   
    parsed_protocols.append(update)
    
for new in parsed_protocols:
    print(new)        