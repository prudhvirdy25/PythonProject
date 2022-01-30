# This code explains how can we
# use 'any' function on list
list1 = []
list2 = []

# Index ranges from 1 to 10 to multiply
for i in range(1,11):
	list1.append(4*i)
print(list1)

# Index to access the list2 is from 0 to 9
for i in range(0,10):
    print(i,list1[i],list1[i]%5,sep=" ")
    list2.append(list1[i]%5==0)

print(list2)

print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))

#******* All Operator *******
# Illustration of 'all' function in python 3

# Take two lists
list1=[]
list2=[]

# All numbers in list1 are in form: 4*i-3
for i in range(1,21):
	list1.append(4*i-3)
print(list1)

# list2 stores info of odd numbers in list1
for i in range(0,20):
    print(i,list1[i],list1[i]%5,sep=" ")
    list2.append(list1[i]%2==1)
print(list2)

print('See whether all numbers in list1 are odd =>')
print(all(list2))

