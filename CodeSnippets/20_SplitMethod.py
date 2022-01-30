# Program  to use  Split method

CustName="Prudhvi,Reddy"
# taking two inputs at a time
CustFirstName, CustLastName=CustName.split(",")
print("FirstName Is:",CustFirstName)
print("LastName Is:",CustLastName)

# taking multiple inputs at a time
# and type casting using list() function
CustName2="A B C D E F G H"
x=list(map(str,CustName2.split()))
print(x)
