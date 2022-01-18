# Logical Expression: evaluate to True or False 
# Logical Operators:  and, or, not

from time import process_time_ns


num1 = 10
num2 = 20

# Comparison operator compare values
# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to 
# >= 	greater than or equal to
# !=    Not equal to
print('The and operator ')
print(num1==15)
print(num1==10)
print(num1==num2)


print(num1==10 and num2==20 )

print(num1==10 or num2==20 )
print(num1==10 or num2==15 )

# not operator
print('The not',not(num1==10 and num2==20 ))

# exercise 2 
# use the not operator with 
# and to evaluate the rxpression to False
# or to evaluate to true and false

print('The not',not(num1==10 or num2==15 ))
print('The not',not(num1==11 or num2==15))
