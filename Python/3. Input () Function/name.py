# input function: allow the program to take input from the user
# The default data type of the input function is a string

from os import name


username = "Paul " # Static Values
print(username)

username = "Jane" # Reasigned the values of username

# First Method
print("What is your firstname")
fname = input() # invoke/ call the input fuction to capture data from the user 

print(f"your name is {fname}")

# Second Method
lname = input("What is your lastname: ")
print(f"your name is : {lname} ")

# concatenate : join together
fullname = fname+ " " + lname

print(f"Your Fullname is {fullname}")
