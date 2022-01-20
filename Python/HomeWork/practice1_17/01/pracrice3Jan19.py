
# Task1: 
# Write a countdown timer program
# •	That will countdown from 60 
# •	 Decrease the count by 1 every time
# •	Print the count


counter = 60
for counter in range(61,0,-1):
    print(counter)


# Task2:
# Research casting in python programming
# https://www.w3schools.com/python/python_casting.asp
# Use the required constructor function to construct 
# Float to integer 
# •	23.4
# •	1.6
# •	2.8
# Integer to float
# •	1234
# •	2
# •	67

x = int(23.4)
y = int(1.6)
z = int(2.8)

print(f"{x} , {y} , {z} ")

a = float(1234)
b = float(2)
c = float(67)

print(f"{a} , {b} , {c} ")

# Task3 
# Write a pseudocode for the multiplication table program below

num1 = int(input("Enter a number : "))
for multiplyby in range (1,13):
    print(f"{num1} x {multiplyby} = {num1 * multiplyby}")    


# ask user for a number to be used in the multiplication

# then comapre the range i loop stating from 1 till the user input 
# multiply the userinput by range 



# Task4:
# What is the difference between While Loop and For Loop; explain with screenshot of your program
# Why is data validation important when user input is required?
# Explain casting in python programming

# while loop is iteration that will excute until the condition is not met while for loop depends with range by referni gto start end and step. 

# Data validation is important because it gives avoid unnesessary errors that may cause the programs with wrong user input

# Casting in pyrhon is use to convert the data types of variable to another datatype