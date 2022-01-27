try:    
    num1 = 10
    num2 = 2

    munDiv = num1/num2
    print(munDiv)
except ZeroDivisionError:
    print("you can't divide a number zeto\nEnter a number that is not zero")
finally: # 
    print("Closing a the program")
