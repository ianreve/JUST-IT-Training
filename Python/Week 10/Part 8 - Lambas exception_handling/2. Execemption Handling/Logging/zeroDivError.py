
import logging
from xml.dom import ValidationErr  # import logging

# set the logging levels
# logging.basicConfig(filename="LogFile2.log", level=logging.DEBUG)

"first sample " 
# try:
#     file1 = open("ErrorLog.txt", "a")
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     munDiv = num1/num2
#     file1.write(f"\nDivision in progress\n the ansers is {munDiv}")
#     print(munDiv)
# except ZeroDivisionError:
#     print("You can't dive a number by zero\nEnter a number that is not Zero")
#     file1.write(f"\nYou can't dive a number by zero\nEnter a number that is not Zero")
# finally:# will execute regardless if either of the try and except is executed
#     print("Closing the program")
#     file1.close()

"sample 2"
# import logging
# #set the logging levels
# logging.basicConfig(filename="LogFile2.log", level=logging.DEBUG)

# try:
#     file1 = open("ErrorLog.txt", "a")
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     munDiv = num1/num2
#     logging.info("Division in progress")
# except ZeroDivisionError:
#     logging.error("You can't dive a number by zero\nEnter a number that is not Zero")
# finally:# will execute regardless if either of the try and except is executed
 
#     file1.close()

# erxercise log error to a file or to a logfile when a user type in a wrong password/name

# logging.basicConfig(filename="LogFile2.log", level=logging.DEBUG)
# try:
#     password = "1234"
#     userPassword = input("Enter your password: ")
#     checkPassword = list(filter(lambda password: password == userPassword))
#     logging.info(f"{checkPassword(userPassword)}password match")
# except ValidationErr:
    
#     logging.error("password didn't macth")

# finally:

import logging

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

try:
    password = input("Enter password: ")

    if password not in ["password", "abcde", "mypassword", "football"]:
        logging.info(f"{password} is secure")
        with open("errorLog.txt", "a") as file:
            file.write(f"{password} is secure\n")
    else:
        logging.warning(f"{password} is insecure")
        with open("errorLog.txt", "a") as file:
            file.write(f"{password} is insecure\n")
except:
    logging.error("An unexpected error occured")
finally:
    print("program has finished executing")
