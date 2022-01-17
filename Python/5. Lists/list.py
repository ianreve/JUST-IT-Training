# items in a list cn be modify
# declare a list1 variable and assign values of different datatpes in the list
# items can be accessed based on their index position

# declare a variable and assign it in a list datatype
from cgi import print_directory
import re


list1 = []
print(list1)

list2 = ["HTML", "CSS"]
print(list2)

# use the insert function to insert an item to a list
list2.insert(0,"Python")
list2.insert(2,"JS")
print(list2)

# Append
list2.append("NoSQL")
list2.append("SDLC")
list2.append("mySQL")
print(list2)

# access list items by index position 
print(list2[4])

# return list length
print("The list length is: ",len(list2))

# ['Python', 'HTML', 'JS', 'CSS', 'NoSQL', 'SDLC', 'mySQL']
print(list2[1:3])
print(list2[2:6])

# delete
del(list2[2])
print(list2)

del(list2[2], list2[4])
print(list2)

# delete/removed items as per their value
list3 = ['Python', 'HTML', 'JS', 'CSS', 'NoSQL', 'SDLC', 'mySQL']
list3.remove('SDLC')
print(list3)

# min and max 
list4 = [1,2,12.5,-5,-10,45]
print("Min",min(list4))
print("Max",max(list4))

# sort list items
list4.sort()
print("Ascending order :", list4)

list4.sort(reverse=True); # reverse order
print("Descending order :", list4)

# ~list exercise
# create a list of 6 items
# insert a new item in postion 3
# add another item to the list
# remove an item by value
# remove the item at index position 3
# for every list manipulation print the list