# A variable holds a value in a memory location that is need
#  for the execution of the program.
#A variable can hold one value at a time . This value can change 
#throughout the execution of the program

# variable must be declared before they can be used 
# declare a variable called num1 and assign the value 10
# =/equal to is an assignment operator in python

# declared num1 variable 
num1 = 10 
num2 = 20 
num3 = 30

print(type(num1))

name = "Ian"
print(type(name))

print("My name is", name , "I am ", num1 , "years old")
print("My name is"+ name + "I am "+ str(num1) + "years old")
# f-string

print(f"My name is {name}  I am  {num1}years old")

totalNums = num1 + num2 + num3

answer = totalNums

print(f"The answer to {num1} + {num2} + {num3} is {answer}")

# Exercise 2
# Muliply answer from num1 and num 2 by num3
#save the answer in a variable 
# print the answer

product = (num1 + num2) * num3

print(f"The Product of {num1} and {num2} by {num3} is : {product}")

# variable naming condition 
username = "ianreve" #
userName = "ianreve" #
username1 = "ianreve" #
firstname = "Ian" #
lastname = "Cacao" #
userAge = 23
age = 24

# dont do this 
# AGE = 12 #unless its a constant
# £money = 12 # don't use symbol
# User = "Jane"
# user name = "Paul"