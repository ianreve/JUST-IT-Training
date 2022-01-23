# i      
aList = [0,1,2,3,4,5,6,8,7,9, 21]

bList = [7,9,0,1,2,3,4,5,6,8, 12, 5]

listAB =[
aList[i] + bList[i]
for i in range(len(aList))
]

print(listAB)
