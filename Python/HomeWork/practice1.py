# Write a program that will ask the user for their first name and then their surname and then will display their full name.

from multiprocessing import pool


firstName = input('Enter your First name : ')
lastName = input('Enter your Last name : ')

print(f'Your Fullname is : {firstName} {lastName} ')

#  Write a program that asks for 3 numbers (num1, num2 and num3). Display the output where it adds together num1 and num2 and then multiplies this total by num3.

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
num3 = int(input("Enter the Third Number : "))
totalNum = (num1 + num2) * num3 

print(f"The sum is : {totalNum}")

# Ask the width, length and depth of a swimming pool and then work out the amount of water that the swimming pool will hold in cubic meters.

poolWidth = int(input('Enter the pool width : '))
poolLength = int(input('Enter the pool length : '))
poolDepth = int(input('Enter the pool depth : '))

volume = poolWidth * poolLength * poolDepth

print(f'The pool can hold a maximum of {volume} cubic meters')

# Ask the user to input the number of hours a worker has worked in a week. Ask the user to also enter the amount that worker earns per hour. Work out the total pay the worker should get for the week’s work.

hoursWorked = float(input('Enter total hours worked : '))
hourRate = float(input('Enter your rate per hour : '))

print(f'Your total pay for the week is : £ {hourRate * hoursWorked}')