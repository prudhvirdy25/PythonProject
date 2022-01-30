# Python program to create classes and object instantiation

class customer():

    # A simple class
    # attributes
    custid=1234
    custname="Prudhvi"

    # A sample method
    def getCustDetails(self):
        print("Customer ID is: ", self.custid)
        print("Customer Name is:", self.custname)

# Driver code
# Object instantiation
CustomerObj= customer()

print("Customer Id from Obj is:" , CustomerObj.custid)
print("Customer Name from Obj is:" , CustomerObj.custname)
CustomerObj.getCustDetails()
