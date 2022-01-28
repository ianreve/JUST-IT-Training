class MobilePhone:
    def __init__(self,phoneMake, phoneDesc, phoneModel, phonePrice):
        # variable: make, description, model and price
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice


iphone11 = MobilePhone("Iphone", "Retina", "11",1234.34 )

phoneMake = input("Enter a Phone Brand: ")
phoneDesc = input("Enter a Phone feature:")
phoneModel = input("Enter a Phone Model: ")
phonePrice= float(input("Enter a Phone Price:"))

phone = MobilePhone(phoneMake, phoneDesc, phoneModel, phonePrice)



print(phone.make)
print(phone.description)
print(phone.model)
print(phone.price)


