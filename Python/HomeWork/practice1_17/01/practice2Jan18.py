from operator import length_hint
from pickletools import pystring
from tkinter import INSERT
from urllib.parse import uses_relative


city = ["London","New York","Manila", "Paris", "Tokyo","Oslo","Porto","Rome","Tromso","Seoul"]

# •	Print the list with all the items showing on one line.
print(city[0],city[1],city[3],city[4],city[5],city[6],city[7],city[8],city[9])

# •	Insert a new city in index position 4
city.insert(3, "Berlin")
print(city)

# •	Print out the fourth item in the list by it index position.
print(city[3])

# •	Print out the sixth item in the list by its value.
print(city[6])

# •	Remove any  two cities from the list
del(city[2],city[5])
print(city)

# •	How can you print the 4th,5th,6th and 7th cities in the list
print(city[3],city[4],city[5],city[6],)

# •	Return the length of the list
print(len(city))

# •	Sort the list in ascending order
city.sort()
print(city) 

# •	Sort the list in descending order
city.sort(reverse=True)
print(city) 


# Task 2

userString = " Python is my third programming language"

# •	Print the 1st, 3rd, 6th, 9th and 11th characters from the string (userString) provided above.
print(userString[0],userString[2],userString[5],userString[8] )

# •	Return the length of the string
print(len(userString))

# •	Slice the string to print between the 3rd and 11 characters

print(userString[2:11])

# •	Omit the last  and  then second to last characters from your string in your print out
length = len(userString)
print(userString[len(userString)-1], userString[len(userString)-2]) 
print(userString[:len(userString)])

# •	Print up to the 15 character from your string.
print(userString[:16])

# •	Find the start index position of the substring “third”
print(userString.find("third"))

# •	Print out the string in all capital letters. 
print(userString.upper())

# •	Print out the string in all non lower case letters. 

print(userString.lower())

# •	Print out the first letter of all the sub strings in capital letters.
print(userString.title())

# •	Replace the substring “third” to so that the string will reflect if it is your first or second…etc 
print(userString.replace("third", "second\n"))


# Task 3

# sweets = int(input("How many sweets in the bag: "))
# numberOfPeople = int(input("How many people to share : "))

# sweetsPerPerson = sweets // numberOfPeople
# sweetsRemaining= sweets % numberOfPeople
# print(f"Each person will have  {sweetsPerPerson} sweets  and still {sweetsRemaining} left in the bag.")

# Task 4 
# import random
from random import randint
randNums1 = randint(1,6)
randNums2 = randint(1,6)
print("The random number is ",randNums1)
print("The random number is ",randNums2)
print("\nThe random number are ",randNums1, randNums2)

if randNums1 == randNums2:
    print("Double is Thrown")
else:
    print(f"You thrown {randNums1} and {randNums2}")

# Task 5 
userInput = int(input("Enter number between 1 - 10 : "))

if userInput <= 10:
        randNums3 = randint(1,10)
        if userInput == randNums3:
            print("Double is trown")
        else:
            print(f"You input {userInput} and thrown is  {randNums3}")
else:
    print("Input should be below 10")