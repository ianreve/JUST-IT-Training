# To understand the meaning of classes we
# have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is
#  always executed when the class is being initiated.
#  Use the __init__() function to assign values to object
#  properties, or other operations that are necessary to do
#  when the object is being created:

class MobilePhone:
    def __init__(self):
        # variable: make, description, model and price
        self.make = ""
        self.description = ""
        self.model = ""
        self.price = 0

# iphone11 = MobilePhone()
# iphone11.make = "Iphone"
# iphone11.description = "Retina Dispplay"
# iphone11.model = "11"
# iphone11.price = 1234.34

# print(iphone11.make)
# print(iphone11.description)
# print(iphone11.model)
# print(iphone11.price)

class MobilePhone:
    def __init__(self):
        # variable: make, description, model and price
        self.make = ""
        self.description = ""
        self.model = ""
        self.price = 0
phone = MobilePhone()

phone.make = input("Enter a Phone Brand: ")
phone.description = input("Enter a Phone feature:")
phone.model = input("Enter a Phone Model: ")
phone.price= input("Enter a Phone Price:")

print(phone.make)
print(phone.description)
print(phone.model)
print(phone.price)



