file1 = open("users.txt", "a")

fname = input("Enter your firstname: ")
lname = input("Enter your lastname: ")
# userDetails = "\n" +fname+ " "+lname


# writeToFile = file1.write(userDetails)

# writeToFile = file1.write("\n" +fname+ " "+lname)
# file1.close()

# method 3 
userData = []
userData.append(fname)
userData.append(lname)
print(userData)
strData = str(userData)

file1.write(strData)
file1.close()

