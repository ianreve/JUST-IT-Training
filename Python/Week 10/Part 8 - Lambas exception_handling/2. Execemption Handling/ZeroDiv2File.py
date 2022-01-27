from gettext import find
import logging
   
password= "password"
userPassword = input("Enter your password: ")
checkPassword = filter(lambda password: password == userPassword)
print(f"{checkPassword(userPassword)}password match")
