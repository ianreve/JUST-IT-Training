def answerYN():
    userResponse = input("Enter y o n")
    while userResponse not in("y","n"):
        print("You must enter y or n ")
        userResponse = input("Please... Enter y or n")
        return userResponse

    answer =  answerYN()
print("Response = ",answerYN)




        