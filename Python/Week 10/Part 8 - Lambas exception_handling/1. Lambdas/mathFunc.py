# The map function expects two arguments: a function and a list.
# It takes that function and applies it to every element in the list, 
# returning the list of modified elements as a map object. 
# The list function is used to convert the resulting map object back into a list again.

# listofNums = [1,2,3,4,5,6,7,8,9,10]
# userNumber = int(input("Enter a number: "))
# lstResults = list(map(lambda num :num * userNumber, listofNums ))
# print(lstResults)

# for evenNums in lstResults:
#     print(evenNums)

listofNums = [1,2,3,4,5,6,7,8,9,10]
userNumber = int(input("Enter a number: "))
lstResults = list(map(lambda num :num * userNumber, listofNums ))
print(lstResults)

for qoutient in lstResults:
    # for i in (listofNums):
        print(f" x {userNumber} = {qoutient}")

 