# Examples of Arithmetic Operator
a = 2
b = 3

# Addition of numbers
add = a + b  #5

# Subtraction of numbers
sub = a - b #-1

# Multiplication of number
mul = a * b #6

# Division(float) of number
div1 = a / b  #.6666

# Division(floor) of number
div2 = a // b #0

# Modulo of both number
mod = a % b #2

# Power
p = a ** b #8

# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)

# *****************************Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

# *****************************Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

# Examples of Bitwise operators
a = 10
b = 4

# *****************************Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)

# ***************************** Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)

# ********** Identity Operator is not, is
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# ********** MemberShip Operator  not in, in
# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")

