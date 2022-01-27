# With the filter function, the process is much the same. 
# Filter takes a function and applies it to every element 
# in a list and created a new list with only the elements 
# that caused the function to return True.

names = ["Anna", "Lucy", "Paul", "Joanne"]
user = input("Enter a name: ")
searchName = list(filter(lambda username: username == user, names))
print("Found", searchName)
