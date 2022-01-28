class MobilePhone:
    def __init__(self,phoneMake, phoneDesc, phoneModel, phonePrice):
        # variable: make, description, model and price
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice



listofPhones = [ ]

while True:
    addMobile = MobilePhone(
        input("Enter a Phone Brand: \n"),
        input("Enter a Phone feature: \n"),
        input("Enter a Phone Model: \n"),
        float(input("Enter a Phone Price: \n"))
        )

    listofPhones.append(f"{addMobile.make} {addMobile.description}  {addMobile.model}  £ {str(addMobile.price)}")
    anotherMobile = input("Add another mobile Y/N: ".upper())
    
    if anotherMobile == "N":
        break # stop user for input
    
print(listofPhones)

for mobile in listofPhones:
    print(mobile)

phoneList = str(listofPhones)
phoneFile = open("MobilePhones.txt", "a")
addToFile = phoneFile.write(phoneList)
phoneFile.close()


# print(phone.make)
# print(phone.description)
# print(phone.model)
# print(phone.price)


