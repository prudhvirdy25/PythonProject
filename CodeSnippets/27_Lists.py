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

#changes to use insert() method

listinsert=[1,3,7,9]
# Addition of Element at
# specific Position
# (using Insert Method)
listinsert.insert(3,"Prudhvi")
print("\n  list after insert operation")
print(listinsert)

#changes to use extend() method
listextend=[1,3,4,5,6]

listextend.extend(["Prudhvi","Reddy","N",1,2,3,4])
print("\n  list after extend operation")
print(listextend)

# negative Indexing to get the elements from the end
print(listextend[-2])

# remove the elements 
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
 
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)
