# from ast import Num


# def even_Odd(a):
#     if a%2 == 0:
#         return "Even Number"
#     else:
#         return "Odd Number"
# solution = even_Odd(110)

# print(f"The asnwer is {solution}")






def highest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number :"))

result = highest(num1, num2)

print(f"{result} is the highest number")
