# Python program to illustrate
# function with main
def getInteger():
    num=int(input("Enter the number;"))
    return num

def Main():
    print("Execution","Started",sep="_")

    output=getInteger()
    print(output)

# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    Main()
