# Program to create different  types of lists

#creating blank list
list=[]
print(int(len(list)))

list.append(1)
list.append("Prudhvi")
list.append((3,4))

list2=["Dummuy","Dummy1"]
list.append(list2)

print(list)


#creting a list with all the numbers
listnum=[1,2,3,4,5]
print(listnum)

#creating a list with strings
liststr=["Prudhvi","Reddy","N"]
print(liststr) 

#Accesing the list by Index values
print(liststr[0])
print(liststr[1])
print(liststr[2])

#creating a list with multiple datatypes
listmul=["Prudhvi",2, 3.5]
print(listmul)

#creating multi lists/nested lists
listnested=[["Prudhvi","Reddy"],"Nallavadla"]
print(listnested)
print(listnested[0])
print(listnested[1])