listofNums = [1,2,3,4,5,6,7,8,9,10,12,4,18,56,86]

print("number of items in original list ", len(listofNums))

lstResults = list(filter(lambda num:num%2==0, listofNums))

print("number of items in original list ", len(lstResults))
print("These are the even numbers in the list ", lstResults)
