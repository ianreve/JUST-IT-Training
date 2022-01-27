from ast import Num
from functools import reduce


listofNums = [1,2,3,4,5,6,7,8,9,10,11,12]


lstResults = reduce(lambda num1, num2: num1 + num2,  listofNums)
print(lstResults)