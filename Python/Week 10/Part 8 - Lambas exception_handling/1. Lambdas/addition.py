# A lambda is simply a way to define a function in Python. They are sometimes known as "lambda 
# operators" or "lambda functions".  A lambda function is a small anonymous function, they are functions
# that don't need to be named. They are used to create small, one-off functions in cases where a "real "
# function would be too big and bulky.   A lambda function can take any number of arguments, but can 
# only have one expression. lambda arguments : expression .

# Lambdas return a function object, which can be assigned to a variable. Lambdas can have any number
#  of arguments, but they can only have one expression. You cannot call other functions inside lambdas.
"Lambda argument: expression"
# variable lambda args: expression
# addTwoNums = lambda num:num + 10 # the expression is num + 10
# print("\nThe answer is : ",addTwoNums((2))) # number 2 get passed is an argumnet

addTwoNums = lambda num1,num2:num1 + num2 
print("\nThe answer is : ",addTwoNums((2),(2)))


addTwoNums2 = lambda num1 = int(input("Enter the First Number: ")) , num2 = int(input("Enter the Second Number: ")): num1 + num2 
print("\nThe answer is : ",addTwoNums2())