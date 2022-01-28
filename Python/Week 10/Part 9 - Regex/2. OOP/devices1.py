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
        self.make = "Samsung"
        self.description = "Slim Build, Touch Screen"
        self.model = "Galaxy S10"
        self.price = 674.45
# how do we acces the properties and value in out class ?
sMobile1 = MobilePhone() # create instance object from moblie class
print(sMobile1.make)
print(sMobile1.description)
print(sMobile1.model)
print(sMobile1.price)

iphone11 = MobilePhone()
iphone11.make = "Iphone"
iphone11.description = "Retina Dispplay"
iphone11.model = "11"
iphone11.price = 1234.34

print(iphone11.make)
print(iphone11.description)
print(iphone11.model)
print(iphone11.price)



