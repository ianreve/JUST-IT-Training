from cgi import test


class MobilePhone:
    def __init__(self,phoneMake, phoneDesc, phoneModel, phonePrice):
        # variable: make, description, model and price
        self.make = phoneMake
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice
    # creste a method
    def phoneDiscount(self):
        calcDiscount = self.price * 0.2
        discountPrice = self.price - calcDiscount
        print(discountPrice)
    
    # create inner class
    class NetworkProvider:
        def __init__(self, netName): 
            self.networkP = netName



mobile1  = MobilePhone("Iphone", "Retina Display", "11", 1234.67)

mobile1.phoneDiscount()
#  accessing inner class
networkName = MobilePhone.NetworkProvider("EE")

test1= mobile1.NetworkProvider("Three")

print(test1.networkP)


print(networkName.networkP)

# MobilePhone.phoneDiscount() 

