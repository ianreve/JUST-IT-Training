

checkNum = lambda num : 'This is a even number' if (num % 2) == 0  else 'This is an Odd number'
num =int(input("Enter a number: "))
print(checkNum(num))


# use the if else in a lambda function to  check against a user age or name

checkAge = lambda age : "You're under 18" if (age <18)   else "You're over 18 "
age =int(input("Enter your age: "))
print(checkAge(age))

checkUsername = lambda username : "Username is match" if (username == "admin") else "Your username is not match" 
userInput = input("Enter your username: ")
print(checkUsername(userInput))