# Iteration means repeatitions
#  While loop : keeps looping until the xondiotin is met 

from itertools import count

i=0
guessAword = input("Enter your guess word :")
while guessAword != "Python":
    i +=1 
    guessAword = input("Try again : ")

print(f"You have correctly guessed {guessAword}")
print(i)