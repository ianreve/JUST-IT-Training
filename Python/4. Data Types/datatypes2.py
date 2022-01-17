
#List is an ordered sequence of items. It is a very flexible data type in python
# The values in a list doesn't have to be of the same type
# items in a list cn be modify
# declare a list1 variable and assign values of different datatpes in the list
# items can be accessed based on their index position

# declare a variable and assign it in a list datatype

c5List =  []

list1 = [1,2,3,4,5,6,"xyz",21.5,"ABC"]
print(type(list1))
print(list1[5])

# Tuple is a sequence of items that are in order
#and it is not possible to modify the tuples. Therefore,
# tuples are faster than list and the primary use of tuples 
# is to create write protect data 
# # items can be accessed based on their index position


tuple1 = ("Tuple","user", 1,2,3,4,5,6,"user")
tuple2 = ("tuple2") # if there's list it will come as list if no , then default datatype
print(type(tuple1))
print(tuple1)

#Set is a  collection of unique items that are not in order, 
# it is an unordered datatype. Duplicates are eliminated in a set
# Set items cannot be accessed based on their index position

set1 = {1,2,3, "Tom","Anna", 7,8,9.5, "Anna"}
print(type(set1))
print(set1 )

# Dictionary stored data as key value pairs 
# to retrieve a specific value from a dictionary you need to know the key

dictionary1 = {1:"John", 2: "Anna", "name1": "Lucy"}
print(type(dictionary1))
print(dictionary1)