raw_passwords = [
    "password", "Tr0ub4dor&3", "hello", "P@ssw0rd!", "abc",
    "Hunter2!", "qwerty", "S3cur1ty#", "12345678", "N3tw0rk$afe",
    "cat", "Br34ch!ng", "letmein", "F1r3w@ll!", "pass"
]
main = []
special =   "!@#$%^&*()"

for pas in raw_passwords:
    #print(pas)
    if len(pas) >= 8 :
      # print(pas)
       for spe in special:
           if spe  in pas :
            #print(pas)
            main.append(pas)
            break
print(main)
print("Total Valid", len(main))
print("Rejected", len(raw_passwords) - len(main))
            