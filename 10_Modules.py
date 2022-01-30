# Python program to invoke modules and use

import math

def Main():
    num=25.453

    # fabs function is used to get the absolute value of a decimal
    # fabs is part of math module that was imported into this program to use
    output=math.fabs(num)
    print(output)

if __name__ == "__main__" :
    Main()