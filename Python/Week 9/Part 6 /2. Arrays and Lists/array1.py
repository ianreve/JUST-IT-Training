"""An array holds multiple items under one name.
An array is a static data structure. 
An array is fixed in size and can only contain data of the same type. 
The contents can be changed, but items cannot be added or deleted. 
The structure must remain fixed. """

arrayChars = ["Amy", 1, 2, "Paul"] #list
arrayDigits = [0,1,2,3,4,5,6,8,7,9] # an array of digits

print(type(arrayChars))
print(type(arrayDigits))

print("The number",arrayDigits[4])

for digit in arrayDigits:
    print(digit)
