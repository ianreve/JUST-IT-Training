def nums(a,b):
    total = 0
    for counter in range(a,b,+1):
        total = counter
        return total
num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))

answer = nums(num1, num2)

print(answer)
