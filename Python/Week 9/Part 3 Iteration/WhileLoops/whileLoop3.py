
# userPass = input("Enter password: ") # first attemt
# passwordAttemps = 2

# while userPass != "Bootcamp" and passwordAttemps <3:
#     userPass = ("Re-enter password: ")
#     passwordAttemps +=1

# if userPass == "Bootcamp":
#     print("Password valid")
# else:
#     print("Password Invalid")


#create a whle loop 
# ask for user input 
# check the user input with a value of your choice
# set the number of attempts for the user
# display message if the number of attempts is exhausted or not exhausted

sides = 6;

userAnswer = int(input("How many side does a Hexagon have ? :  "))
attempts = 0

while userAnswer != 6 and attempts <3:
    attempts +=1
    userAnswer = int(input("Wrong Answer, try again :  "))

if userAnswer == 6:
       
        print(f"Right answer")
else:
        print(f"Hexagon does not have {userAnswer} and you run of of tries")
