list1 = ["Tom", "Peter", "Harry", "Jane", "Janet", "Ada", "Anna"]
list2 = ["Tom", "Harry", "Jane", "Paul" , "Lucy", "Greg" ]
# list3 = []

list3 = [ names for names in list1 if names in list2]
print(list3)

# exercise 
# create a list of names to search through 
# break out from the loop when the name
#in the list is found
list1 = ["Tom", "Peter", "Harry", "Jane", "Janet", "Ada", "Anna"]
