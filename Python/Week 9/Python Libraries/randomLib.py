from random import randint # import specific module from the library 

# variable = method
randNums1 = randint(1,20)
print(randNums1)

die1 = randint(1,6)
die2 = randint(1,6)

if die1 == die2:
    print(f"You threw double {die1} {die2}")
else:
    print(f"you threw {die1} {die2} ")