
# Program to get emailid and separate it to userid & domainname

emailid="   prudhvi.nallavadla@google.com    "
validemail=emailid.strip()    # strip is used to remove spaces at the begining and at the end of the string

print(int(len(validemail)))



username=emailid[:emailid.index('@')]
domainname=emailid[emailid.index('@')+1:]

print(username)
print(domainname)