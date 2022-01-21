# subroutine is a sequence of insructions/ code block to perform a specific
# task with an identifiable name
# A subroutine does not have a return statement.
# def is a keyword used to dfine a subroutine, followed by the name of the subroutine
# It is not executed unless the subroutine is called.



def username():
    uName = input("Enter your username: ")
       
    print(f"Your username is {uName}, thanks for joining us. ")

username()
    
    
def name():
    firstName = input("Enter your Firstname: ")
    lastName = input("Enter your Lastname: ")
    age = input("Enter your age : ")
    favMovie = input("Enter your favorite Movie : ")
    print(f"Hi {firstName} {lastName} and Favorite movie is {favMovie} ")

name()


